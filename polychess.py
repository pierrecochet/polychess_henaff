# =============================================================================
# IMPORTS 
# =============================================================================
import chess
import chess.polyglot
import chess.pgn
import random
import minMax
import os
import errno
import datetime



# =============================================================================
# GENERAL FUNCTIONS 
# =============================================================================

def findBestMovePolyglot(board):
    """
    Function that returns the best move to play in a list of playable moves, according to the Polyglot book
    Parameters :
        -board : the current board
    Returns :
        -List[move to play, weight of this move]
    """
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        entry=list(reader.find_all(board))
        if(entry==[]):
            return [None,None]
        else:       
            return [str(entry[0].move()), entry[0].weight]

def findRandomMovePolyglot(board):
    """
    Function that returns a random move to play in a list of playable moves, according to the Polyglot book
    Parameters :
        -board : the current board
    Returns :
        -List[move to play, weight of this move]
    """
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        entry=list(reader.find_all(board))
        lenList= len(entry)
        #Returns None,None if there is no move playable
        if(lenList==0):
            return [None,None]
        #returns the first move if there is only one playable move
        if(lenList==1):
            return [str(entry[0].move()), entry[0].weight]
        #If there is more than 1 playable move, returns a random move between the 2nd and the last playable move
        else:       
            moveToPlay= random.randrange(1, lenList)
            return [str(entry[moveToPlay].move()), entry[moveToPlay].weight]

def findRandomMove(board):   
    """
    Function that returns a random move to play in the list of all the playable moves
    Parameters :
        -board : the current board
    Returns :
        - move to play
    """
    #get all the legal moves for the current position
    moves = list(board.legal_moves)
    #get a random int between 0 and the number of legal moves
    if len(moves)>0:
        moveToPlay= random.randrange(0, len(moves))
    #returns None if the player can't move
    else:
        return None
    #returns a random move in this list of moves in UCI format
    return chess.Move.uci(moves[moveToPlay])

def findMovePGthenMinMax(board): 
    """
    Function that returns the best move according to Polyglot, and if there is none, returns
    the best move according to the MinMax algorithm
    Parameters :
        -board : the current board
    Returns :
        - move to play
    """
    move=findBestMovePolyglot(board)[0]
    if move is None:
        move=chess.Move.uci(minMax.minMaxAlphaBeta(board,4,-3000,3000)[1])
    return move

def moveFromInput(board):
    """
    Function that returns a move typed in the console (after having checked if its a legal move)
    Parameters :
        -board : the current board
    Returns :
        - move to play
    """
    validMove=False
    nbTry = 0
    #Asks the player to play until he types a legal move
    while validMove == False:
        #if it's not the first time that the player has to type his move, an error message is displayed
        if nbTry > 0:
            print("This isn't a valid move.")
        #asks the player to type a move to play
        currentMove = input("Please enter the move you want to play. (ex : d2d4, a5a7...)")
        for move in list(board.legal_moves):
            if currentMove == chess.Move.uci(move):
                validMove = True
        nbTry+=1
    return currentMove
        


def getMove(currentBoard,playerType):
    """
    Function that returns a move depending on the type of the current player
    Parameters :
        -currentBoard : the current board
        -playerType(int): the type of the current player
            -1:Played by Polyglot (best move)
            -2:Played by Polyglot (random move)
            -3:Played randomly (random move in the playable moves)
            -4:Played by a human (by the console)
            -5:Played by MinMax (and improved by AlphaBeta) to find the best move
            -6:Played by Polyglot then MinMax when Polyglot doesn't find any move to play
    Returns :
        -move(str): the move to play (in UCI protocol)
            -this move can be equal to None if no move has been found
    """
    if playerType==1:
        move=findBestMovePolyglot(currentBoard)[0]
    if playerType==2:
        move=findRandomMovePolyglot(currentBoard)[0]
    if playerType==3:
        move=findRandomMove(currentBoard)
    if playerType==4:
        move=moveFromInput(currentBoard)
    if playerType==5:
        move=chess.Move.uci(minMax.minMaxAlphaBeta(currentBoard,4,-3000,3000)[1])
    if playerType==6:
        move=findMovePGthenMinMax(currentBoard)
    return move

def playMove(currentBoard,move):
    """
    Function that plays the move in parameter in the current board
    Parameters :
        -currentBoard : the current board
        -move: the move to play in UCI protocol
    Returns :
        This function doesn't return anything.
    """
    moveToDo=chess.Move.from_uci(move)
    currentBoard.push(moveToDo)

def getCurrentPlayer(currentBoard, playerTypeW,playerTypeB ):
    """
    Function that returns the type of the current player (MinMax, human, random...) and its color
    Parameters :
        -currentBoard : the current board
        -playerTypeW : type of the white player
        -playerTypeB : type of the black player
    Returns :
        This function doesn't return anything.
    """
    if currentBoard.turn:
        typeCurrentPlayer=playerTypeW
        currentPlayer="W"
    else:
        typeCurrentPlayer=playerTypeB
        currentPlayer="B"
    return [typeCurrentPlayer,currentPlayer]
    
def gameOver(currentBoard,typeCurrentPlayer):
    """
    Function that checks if the game is over in the current board
    Parameters :
        -currentBoard : the current board
        -typeCurrentPlayer : type of the current player
    Returns :
        - [True, game over message] if the game is over
        - [False, empty string] if the game can continue
    """
    #If the player is only using Polyglot, the game is over when Polyglot doesn't find any
        #move to play anymore
    if(typeCurrentPlayer == 1 or typeCurrentPlayer == 2):
        if (getMove(currentBoard,typeCurrentPlayer) is None):
            return [True, "No move has been found in the Polyglot book."]
    #If the player plays with something else than ONLY PolyGlot (MinMax, console...)
    else:
        if(currentBoard.is_stalemate()):
            return [True, "Stalemate"]
        if(currentBoard.is_insufficient_material()):
            return [True, "Insufficient material"]
        if(currentBoard.is_checkmate()):
            return [True, "Checkmate"]
        if(currentBoard.is_seventyfive_moves()):
            return [True, "The last 75 consecutive moves have been made by each player \
without the movement of any pawn and without the capture of any piece."]
        if(currentBoard.is_fivefold_repetition()):
            return [True, "The same position occured 5 times."]
    return [False,""]

def chessGame(currentBoard, playerTypeW,playerTypeB ):
    """
    Function that plays a chess game until the game is over
    Parameters :
        -currentBoard : the current board
        -playerTypeW : the type of the white player
        -playerTypeB : the type of the black player
    Returns :
        This function doesn't return anything.
    """
    typeCurrentPlayer=getCurrentPlayer(currentBoard,playerTypeW,playerTypeB)[0]
    colorCurrentPlayer=getCurrentPlayer(currentBoard,playerTypeW,playerTypeB)[1]
    turnNumber=1
    print("Beginning of the game :")
    #prints the beginning board
    print(currentBoard)
    #Game loop
    #When gameOver(currentBoard,typeCurrentPlayer)[0] == True, the game is over :  "we" go out of the loop.
    while gameOver(currentBoard,typeCurrentPlayer)[0] == False:
        #Find the next move to play for the current player
        move = getMove(currentBoard,typeCurrentPlayer)
        #Plays this move
        playMove(currentBoard,move)     
        #Displays the turn number if it's the white player turn to play.
        if(colorCurrentPlayer=="W"):
            print("-----------------------")
            print("TURN NUMBER",turnNumber)
            print("\nWHITE MOVE :", move)
        else:
            print("\nBLACK MOVE:", move)
            turnNumber+=1
        #Print the new board, after the move have been played
        print(currentBoard)
        #sets the type and the color of the "new" current player        
        typeCurrentPlayer=getCurrentPlayer(currentBoard,playerTypeW,playerTypeB)[0]
        colorCurrentPlayer=getCurrentPlayer(currentBoard,playerTypeW,playerTypeB)[1]
        
    #Prints GAME OVER when the game is over, and a message to explain why the game is over, depending on the game 
    print("-----------------------")
    print("GAME OVER :",gameOver(currentBoard,typeCurrentPlayer)[1])
            
    
# =============================================================================
#  Storage of every game played in PGN format
# =============================================================================


def createPGN(board, eventName=None, siteName=None, datePGN=None, roundNum=None, whiteName=None, blackName=None):
    """
    Function that creates a file filled with the entire game in PGN format
    Parameters :
        -board : the current board
        -eventName : Name of the event
        -siteName  : Name of the site
        -datePGN   : date of the game, in PGN format
        -roundNum  : Number of the current round
        -whiteName : Name of the white player
        -blackName : Name of the black player
    Returns :
        -Nothing but creates a new file in the games directory
    """
    game = chess.pgn.Game.from_board(board)
    nowPGN = datetime.datetime.now().strftime('%Y.%m.%d')
    game.headers["Event"]='?' if eventName is None else eventName
    game.headers["Site"]='?'  if siteName  is None else siteName
    game.headers["Round"]='?' if roundNum  is None else roundNum
    game.headers["White"]='?' if whiteName is None else whiteName
    game.headers["Black"]='?' if blackName is None else blackName
    game.headers["Date"]=nowPGN if datePGN is None else datePGN
    
    ext = '.txt'
    directory = "games/"
    filename = directory + str(game.headers["Event"]) + " " + str(game.headers["Round"])+ ext
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc : 
            if exc.errno != errno.EEXIST:
                raise
    
    f = open(filename, "w+")
    f.write(str(game))
    f.close()
    
    




# =============================================================================
# TESTING OUR CODE
# =============================================================================
board=chess.Board()
board2 =chess.Board("rn1q1rk1/pppbb1pp/4pn2/3p1p2/2PP4/BP3NP1/P3PPBP/RN1Q1RK1 b - - 2 8")

chessGame(board, 5,6)

#createPGN(board, eventName = "Coupe Du Monde", roundNum = "3")

#-1:Joué par Polyglot (meilleur coup d'après lui)
#-2:Joué par Polyglot (coup aléatoire parmis les coups qu'il propose)
#-3:Joué totalement aléatoirement (parmi les coups possibles)
#-4:Joué par un humain (à travers la console)
#-5:Joué avec MinMax pour trouver le meilleur coup
#-6:Joué avec Polyglot puis MinMax lorsque Polyglot ne trouve plus rien
            

