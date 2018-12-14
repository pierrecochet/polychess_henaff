#python-chess import
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot
#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

#print the board on the console

#print(board.fen)


#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position
#moves = board.legal_moves

def findMovePolyglot(board):
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        entry=list(reader.find_all(board))
        if(entry==[]):
            return None
        else:       
            return [str(entry[0].move()), entry[0].weight, entry[0].learn]

def playMove(currentBoard,moveUci):
    moveToDo=chess.Move.from_uci(moveUci)
    currentBoard.push(moveToDo)

board=chess.Board()
tour=1
print(board)


while (findMovePolyglot(board) is not None):
    print("----------------------")
    if(tour%2==0):
        print("TOUR NOIR : ", findMovePolyglot(board)[1])
    else:
        print("TOUR BLANC : ", findMovePolyglot(board)[1])
    playMove(board,findMovePolyglot(board)[0])
    print(board)
    tour+=1

# Make the move

#print(board)


#how many moves are available?
print(moves.count())

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
    
