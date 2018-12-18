import chess
#used to access Polyglot book
import chess.polyglot


def minMax(board, depth):
    moves = list(board.legal_moves)
    
    if depth == 0 or moves == 0:
        return (evaluate(board), None)
    
    if board.turn :
        maxValue = -10**22
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, bestMove = minMax(board, depth-1)
            board.pop()
            maxValue = max(maxValue, val)
        return maxValue
    else :
        minValue = 10**22
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, bestMove = minMax(board, depth-1)
            board.pop()
            minValue = min(minValue, val)
        return maxValue
        
        
        


