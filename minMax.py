import chess
#used to access Polyglot book
import chess.polyglot


def boardValue(board):
    """
    Fonction qui renvoie la valeur du board. 
    Cette valeur est d'autant positif qu'elle est favorable aux blancs et reciproquement.
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
    Retourne :
        -int(value)
    """
    value=0
    chaine = board.fen()
    for i, char in enumerate(chaine):
        if char == 'q' :
            value -= 8.8
        if char == 'r' : 
            value -= 5.1
        if char == 'b' :
            value -= 3.33
        if char == 'n' :
            value -= 3.2
        if char == 'p' :
            value -= 1 
        if char == 'Q' :
            value += 8.8
        if char == 'R' : 
            value += 5.1
        if char == 'B' :
            value += 3.33
        if char == 'N' :
            value += 3.2
        if char == 'P' :
            value += 1 
        if char == ' ' : 
            break
    return round(value,3)
    

def minMax(board, depth):
    """
    Fonction qui calcule le meilleur coup à jouer en similant les 
    prochain n coups
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
        -depth : nombre de tour simulés
    Retourne :
        Tuples : Valeur de mouvement + mouvement à jouer
    """
    moves = list(board.legal_moves)
    
    if depth == 0 or moves == 0:
        return (boardValue(board), None)
    
    if board.turn :
        maxValue = -float("inf")
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, bestMove = minMax(board, depth-1)
            board.pop()
            if val > maxValue:
                maxValue = val
                bestMove = move
        return (maxValue, bestMove)
    else :
        minValue = float("inf")
        bestMove = None
        for move in moves :
            nextMove = chess.Move.from_uci(chess.Move.uci(move))
            board.push(nextMove)
            val, bestMove = minMax(board, depth-1)
            board.pop()
            if val < minValue:
                minValue = val
                bestMove = move
        return (minValue, bestMove)
        
board = chess.Board()
print(minMax(board, 4))

