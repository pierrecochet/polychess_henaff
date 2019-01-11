#python-chess import 
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot

#set the initial position
board1 = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
board2 = chess.Board('rn1q1rk1/pppbb1pp/4pn2/3p1p2/2PP4/BP3NP1/P3PPBP/RN1Q1RK1 b - - 2 8')

#access the Polyglot book
with chess.polyglot.open_reader("polychesshenaff.bin") as reader:
    for entry in reader.find_all(board2):
        print(entry.move(), entry.weight, entry.learn)

