# =============================================================================
# VALUES OF EACH PIECE DEPENDING ON THEIR POSITION
# =============================================================================

valuesKing=[[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
            [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]]

valuesQueen=[[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
             [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
             [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
             [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
             [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
             [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
             [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
             [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]

valuesRook=[[  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
            [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]

valuesBishop=[[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
              [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
              [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
              [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
              [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
              [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
              [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
              [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]

valuesKnight=[[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
              [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
              [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
              [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
              [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
              [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
              [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
              [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]

valuesPawn=[[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
            [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
            [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
            [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
            [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
            [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]



def boardToArray(board): 
    """
    Function that plays a chess game until the game is over
    Parameters :
        -currentBoard : the current board
        -playerTypeW : the type of the white player
        -playerTypeB : the type of the black player
    Returns :
        This function doesn't return anything.
    """
    #remplacement des nombres dans la chaine par un nombre de tirets équivalent
    board = board.replace("1","-").replace("2","--").replace("3","---").replace("4","----")\
        .replace("5","-----").replace("6","------").replace("7","-------").replace("8","--------")
    currentLine=[]
    arrayBoard=[]
    for i,char in enumerate(board):
        #au premier espace rencontré, on arrête le parcours de la chaine et on rentre dans une nouvelle case la dernière ligne parcourue
        if(char==' '):
            arrayBoard.append(currentLine)
            break
        #si on rencontre un slash "/", on créé une nouvelle case dans la liste qui contient la nouvelle ligne parcourue
        if((i+1)%9==0):
            arrayBoard.append(currentLine)
            currentLine=[]
        #ajout du caractère parcouru dans la ligne en cours
        else:
            currentLine.append(char)
    return(arrayBoard)

def returnBlackPlayer(arrayBoard):
    for i,line in enumerate(arrayBoard):
        for j,char in enumerate(line):
            #S'il n'y a qu'un caractère dans la case, on la traite (ainsi, on ne traitera pas les cases où
            #un changement de position d'une pièce noire a déjà été fait)
            if(len(char)==1):
                #Si ce caractère est une majuscule
                if(char.islower()):
                    arrayBoard[7-i][7-j]=arrayBoard[7-i][7-j].replace("-","_")+char
                    arrayBoard[i][j]='-'
    return arrayBoard

def getValueCell(cell,i,j):
    valueCell=0
    if "p" in cell:
        valueCell+=(-1)*(10+valuesPawn[i][j])
    if "P" in cell:
        valueCell+=10+valuesPawn[i][j]
    if "r" in cell:
        valueCell+=(-1)*(51+valuesRook[i][j])
    if "R" in cell:
        valueCell+=51+valuesRook[i][j]
    if "n" in cell:
        valueCell+=(-1)*(32+valuesKnight[i][j])
    if "N" in cell:
        valueCell+=32+valuesKnight[i][j]
    if "b" in cell:
        valueCell+=(-1)*(33.3+valuesBishop[i][j])
    if "B" in cell:
        valueCell+=33.3+valuesBishop[i][j]
    if "q" in cell:
        valueCell+=(-1)*(88+valuesQueen[i][j])
    if "Q" in cell:
        valueCell+=88+valuesQueen[i][j]
    if "k" in cell:
        valueCell+=(-1)*(900+valuesKing[i][j])
    if "K" in cell:
        valueCell+=900+valuesKing[i][j]
    return valueCell

def getBoardEval(board):
    arrayBoard=boardToArray(board.fen())
    reversedBlack=returnBlackPlayer(arrayBoard)
    valueEval=0
    for i,line in enumerate(reversedBlack):
        for j,char in enumerate(line):
            valueEval+=getValueCell(reversedBlack[i][j],i,j)
    return valueEval
            
                    



