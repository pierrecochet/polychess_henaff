#python-chess import
#https://github.com/niklasf/python-chess
import chess
#used to access Polyglot book
import chess.polyglot
import random


def findBestMovePolyglot(board):
    """
    Fonction qui renvoie le meilleur move a jouer parmi la liste des moves jouables, d'apres Polyglot
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
    Retourne :
        -List[move a jouer, poids du move, learn]
    """
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        entry=list(reader.find_all(board))
        if(entry==[]):
            return [None,None,None]
        else:       
            return [str(entry[0].move()), entry[0].weight, entry[0].learn]

def findRandomMovePolyglot(board):
    """
    Fonction qui renvoie un move aleatoire a jouer parmi la liste des meilleurs move, d'apres Polyglot
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
    Retourne :
        -List[move a jouer, poids du move, learn]
    """
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        entry=list(reader.find_all(board))
        lenList= len(entry)
        #S'il n'y a aucun coup a jouer, on return None
        if(lenList==0):
            return [None,None,None]
        #S'il n'a qu'un coup restant d'apres Polyglot, on le joue
        if(lenList==1):
            return [str(entry[0].move()), entry[0].weight, entry[0].learn]
        #S'il y a plus d'un coup jouable, on utilise randrange pour jouer un coup aleatoire parmis les coups,
        #en excluant le meilleur coup
        else:       
            moveToPlay= random.randrange(1, lenList)
            return [str(entry[moveToPlay].move()), entry[moveToPlay].weight, entry[moveToPlay].learn]

def findRandomMove(board):
    """
    Fonction qui renvoie un move aleatoire a jouer parmi la liste des moves possibles
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
    Retourne :
        -string : move a jouer
    """
    #get all the legal moves for the current position
    moves = list(board.legal_moves)
    #get a random int between 0 and the number of legal moves
    if len(moves)>0:
        moveToPlay= random.randrange(0, len(moves))
    #return None if the player can't move
    else:
        return None
    #return a random move in this list of moves in UCI format
    return chess.Move.uci(moves[moveToPlay])


def getMove(currentBoard,typeJoueur):
    """
    Fonction qui retourne un coup en fonction du type du joueur actuel
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
        -typeJoueur(int): le type du joueur actuel
            -1:Joué par Polyglot (meilleur coup d'après lui)
            -2:Joué par Polyglot (coup aléatoire parmis les coups qu'il propose)
            -3:Joué totalement aléatoirement (parmi les coups possibles)
            -4:Joué par un humain (à travers la console)
            -5:Joué avec MinMax pour trouver le meilleur coup
            -6:Joué avec Polyglot puis MinMax lorsque Polyglot ne trouve plus rien
    Retourne :
        -move(str):le move a jouer en format FEN
            Ce move peut valoir None si aucun coup n'a été trouvé
    """
    if typeJoueur==1:
        move=findBestMovePolyglot(currentBoard)[0]
    if typeJoueur==2:
        move=findRandomMovePolyglot(currentBoard)[0]
    if typeJoueur==3:
        move=findRandomMove(currentBoard)
    if typeJoueur==4:
        pass
    if typeJoueur==5:
        pass
    return move

def getCurrentPlayer(currentBoard,typeJoueurW,typeJoueurB):
    if currentBoard.turn:
        typeCurrentPlayer=typeJoueurW
        currentPlayer="W"
    else:
        typeCurrentPlayer=typeJoueurB
        currentPlayer="B"
    return [typeCurrentPlayer,currentPlayer]

def playMove(currentBoard,move):
    """
    Fonction qui joue un coup en fonction du type du joueur actuel
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
        -move: le move a jouer en format FEN
    Retourne :
        Aucun retour, le coup est simplement joué
    """
    moveToDo=chess.Move.from_uci(move)
    currentBoard.push(moveToDo)
    
def gameOver(currentBoard,typeCurrentPlayer):
    print(list(currentBoard.legal_moves))
    #Si le joueur actuel se sert uniquement de Polyglot, on provoque le GameOver 
    #lorsque Polyglot ne propose plus aucun coup à jouer
    if(typeCurrentPlayer == 1 or typeCurrentPlayer == 2):
        if (getMove(currentBoard,typeCurrentPlayer) is None):
            return [True, "Aucun move n'a été trouvé dans Polyglot"]
    #Si le joueur actuel ne se sert pas d'uniquement Polyglot (Aléatoire, humain...)
    else:
        if(currentBoard.is_stalemate()):
            return [True, "Le joueur est en pat"]
        if(currentBoard.is_insufficient_material()):
            return [True, "Matériel insuffisant"]
        if(currentBoard.is_checkmate()):
            return [True, "Echec et mat"]
        if(currentBoard.is_seventyfive_moves()):
            return [True, "75 tours sont passés sans capture ni mouvement de pion"]
        if(currentBoard.is_fivefold_repetition()):
            return [True, "La même position est apparue 5 fois de suite"]
    return [False,""]

def chessGame(currentBoard,typeJoueurW,typeJoueurB):
    #Trouve le type du joueur actuel 
    typeCurrentPlayer=typeJoueurW
    colorCurrentPlayer=getCurrentPlayer(currentBoard,typeJoueurW,typeJoueurB)[1]
    numeroTour=1
    print("Début de la partie :")
    print(currentBoard)
    #Boucle du jeu
    while gameOver(currentBoard,typeCurrentPlayer)[0] == False:
        
        if(colorCurrentPlayer=="W"):
            print("-----------------------")
            print("TOUR",numeroTour)
            print("Coup BLANC :")
        else:
            print("\nCoup NOIR:")
            numeroTour+=1
        playMove(currentBoard,getMove(currentBoard,typeCurrentPlayer))       
        if currentBoard.turn:
            typeCurrentPlayer=typeJoueurW
        else:
            typeCurrentPlayer=typeJoueurB
        print(currentBoard)
        typeCurrentPlayer=getCurrentPlayer(currentBoard,typeJoueurW,typeJoueurB)[0]
        colorCurrentPlayer=getCurrentPlayer(currentBoard,typeJoueurW,typeJoueurB)[1]
    print("Fin de la partie : ",gameOver(currentBoard,typeCurrentPlayer)[1])
            
    
    

board=chess.Board()
board2 = chess.Board("rn1q1rk1/pppbb1pp/4pn2/3p1p2/2PP4/BP3NP1/P3PPBP/RN1Q1RK1 b - - 2 8")
print(board)
tour=1
#chessGame(board,3,3)
#-1:Joué par Polyglot (meilleur coup d'après lui)
#-2:Joué par Polyglot (coup aléatoire parmis les coups qu'il propose)
#-3:Joué totalement aléatoirement (parmi les coups possibles)
#-4:Joué par un humain (à travers la console)
#-5:Joué avec MinMax pour trouver le meilleur coup
            
        
        
    

# Make the move

#print(board)


#how many moves are available?
#print(moves.count())

#iterate over all the moves
#for move in moves: 
#    
#    #display the move
#    print(move)    #save the current position
#    current_board = board
#    
#    #do the move
#    board.push(move)
#    
#    #display the board
#    print(board)
#    
#    #number of black moves
#    print("Black moves:" + str(board.legal_moves.count()))
#    
#    #undo the move
#    board.pop()
#    
#    #do we have a winner?
#    if (board.is_game_over()):
#        print("The game is over")
#        print(board.result())
    
