import chess
import chess.polyglot
import evaluation as ev
    
def minMax(board, depth):
    """
    [DEPRECIATED - SEE THE FUNCTION "minMaxAlphaBeta"]
    Function that calculates the best move to play, considering that the opponent will use the same algorithm
        and will also play the best theorical move, recursively
    Parameters :
        -board : the current board
        -depth : number of turns simulated after the current one : 
            the bigger this parameter is, the more precise the algorithm is
    Returns :
        Tuples : (Value of the move, move)
    """
    moves = list(board.legal_moves)
    if depth == 0 or moves == 0:
        return (ev.getBoardEval(board), None)
    
    
    if board.turn :
        bestMove = None
        maxValue = -3000
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, currentMove = minMax(board, depth-1)
            board.pop()
            if val > maxValue:
                maxValue = val
                bestMove = move
        return (maxValue, bestMove)
    else :
        minValue = 3000
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, currentMove = minMax(board, depth-1)
            board.pop()
            if val < minValue:
                minValue = val
                bestMove = move
        return (minValue, bestMove)

def minMaxAlphaBeta(board, depth, alpha, beta):    
    """
    Function that calculates the best move to play, considering that the opponent will use the same algorithm
        and will also play the best theorical move, recursively
        The difference with the basic minMax function is the Alpha–beta pruning, a search 
        algorithm that seeks to decrease the number of nodes that are evaluated by the minMax 
        algorithm in its search tree.
    Parameters :
        -board : the current board
        -depth : number of turns simulated after the current one : 
            the bigger this parameter is, the more precise the algorithm is
        -alpha : the minimum score that the maximizing player is assured of
        -beta : the maximum score that the minimizing player is assured of
    Returns :
        Tuples : (Value of the move, move)
    """
    moves = list(board.legal_moves)
    if depth == 0 or moves == 0:
        #When we are at the "deepest" level of the reccurence, returns the evaluation of the current board
        return (ev.getBoardEval(board), None)
    
    if board.turn :
        bestMove = None
        maxValue = -3000
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, currentMove = minMaxAlphaBeta(board, depth-1, alpha, beta)
            board.pop()
            if val > maxValue:
                maxValue = val
                bestMove = move
            alpha=max(alpha,val)
            if beta <= alpha:
                break
        return (maxValue, bestMove)
    else :
        minValue = 3000
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, currentMove = minMaxAlphaBeta(board, depth-1, alpha, beta)
            board.pop()
            if val < minValue:
                minValue = val
                bestMove = move
            beta=min(beta,val)
            if beta <= alpha:
                break
        return (minValue, bestMove)        
    
    
