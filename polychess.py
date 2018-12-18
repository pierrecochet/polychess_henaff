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
            return None
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
            return None
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
    moveToPlay= random.randrange(0, len(moves))
    #return a random move in this list of moves
    return moves[moveToPlay]


def playMove(currentBoard,typeJoueur):
    """
    Fonction qui joue un coup en fonction du type du joueur actuel
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
        -typeJoueur(int): le type du joueur actuel
            -1:Joué par Polyglot (meilleur coup d'après lui)
            -2:Joué par Polyglot (coup aléatoire parmis les coups qu'il propose)
            -3:Joué totalement aléatoirement (parmi les coups possibles)
            -4:Joué par un humain (à travers la console)
            -5:Joué avec MinMax pour trouver le meilleur coup
    Retourne :
        Aucun retour, le coup est simplement joué
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
    moveToDo=chess.Move.from_uci(move)
    currentBoard.push(moveToDo)

board=chess.Board()
tour=1
print(board)
print(board.legal_moves.count())
print(findRandomMove(board))



# ALGORITHME QUI FAIT JOUER L'ALGORITHME POLYGLOT CONTRE LUI-MEME
#while (findBestMovePolyglot(board) is not None):
#    print("----------------------")
#    if(tour%2==0):
#        print("TOUR",,"NOIR: ", findBestMovePolyglot(board)[1])
#    else:
#        print("TOUR BLANC : ", findBestMovePolyglot(board)[1])
#    playMove(board,findBestMovePolyglot(board)[0])
#    print(board)
#    tour+=1



# ALGORITHME QUI FAIT JOUER L'ALGORITHME POLYGLOT CONTRE UN BOT "ALEATOIRE" QUI UTILISE POLYGLOT
#while (findRandomMovePolyglot(board) is not None):
#    print("----------------------")
#    if(tour%2==0):
#        randomMove=findRandomMovePolyglot(board)
#        print("TOUR NUMERO",tour,"NOIR : ", randomMove[1])
#        playMove(board,randomMove[0])
#    else:
#        print("TOUR NUMERO",tour,"BLANC : ", findBestMovePolyglot(board)[1])
#        playMove(board,findBestMovePolyglot(board)[0])
#    print(board)
#    tour+=1
    
# ALGORITHME QUI FAIT JOUER L'ALGORITHME POLYGLOT CONTRE UN BOT "ALEATOIRE" COMPLETEMENT
#while (findRandomMovePolyglot(board) is not None):
#    print("----------------------")
#    if(tour%2==0):
#        randomMove=findRandomMove(board)
#        print("TOUR NUMERO",tour,"NOIR : ")
#        playMove(board,randomMove)
#    else:
#        print("TOUR NUMERO",tour,"BLANC : ", findBestMovePolyglot(board)[1])
#        playMove(board,findBestMovePolyglot(board)[0])
#    print(board)
#    tour+=1


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
    
