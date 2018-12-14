#python-chess import 
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot

#set the initial position
board1 = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
board2 = chess.Board("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1")

#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board2):
        print(entry.move(), entry.weight, entry.learn)

