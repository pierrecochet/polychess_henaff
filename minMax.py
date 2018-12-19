import chess
#used to access Polyglot book
import chess.polyglot
import evaluation as ev


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
    
def getBestNextMove(currentBoard):
    minBlack=3000
    maxWhite=-3000
    bestMove=None
    for move in list(currentBoard.legal_moves):
        nextMove = chess.Move.from_uci(chess.Move.uci(move))
        currentBoard.push(nextMove)
        evalNextMove=getBoardEval(currentBoard.fen())
        currentBoard.pop()
        if currentBoard.turn:
            if evalNextMove>maxWhite:
                maxWhite=evalNextMove
                bestMove=move
        else:
            if evalNextMove<minBlack:
                minBlack=evalNextMove
                bestMove=move
    if currentBoard.turn:
        return [bestMove, maxWhite]
    else:
        return [bestMove, minBlack]
    
    

#def getFullValueMove()
        

        


def minMax(board, depth):
    """
    Fonction qui calcule le meilleur coup à jouer en simulant les 
    prochain n coups
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
        -depth : nombre de tour simulés
    Retourne :
        Tuples : Valeur de mouvement + mouvement à jouer
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
        
board1 = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
board2 = chess.Board('rn1q1rk1/pppbb1pp/4pn2/3p1p2/2PP4/BP3NP1/P3PPBP/RN1Q1RK1 b - - 2 8')



#print(ev.getBoardEval(board2))

print(minMax(board2,3))
#print(list(board2.legal_moves))
#for move in list(board2.legal_moves):
#    nextMove = chess.Move.from_uci(chess.Move.uci(move))
#    board2.push(nextMove)   
#    print(getBestNextMove(board2))
#    board2.pop()
#print(minMax(board, 0))

