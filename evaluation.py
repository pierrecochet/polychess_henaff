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
    Function that converts a board (in FEN notation) in a list of lists of lines of the chess board
    Parameters :
        -board : the current board
    Returns :
        -arrayBoard : a list composed of lists(=lines) of the strings(=pieces)  of the boards
    """
    #replacement of the number in the string by the equivalent number of dashes
    board = board.replace("1","-").replace("2","--").replace("3","---").replace("4","----")\
        .replace("5","-----").replace("6","------").replace("7","-------").replace("8","--------")
    currentLine=[]
    listBoard=[]
    #reads the board string char by char in a 'for' loop
    for i,char in enumerate(board):
        #When a space char ' ' is read, the loop is stopped and the last read line is
            #added to the list of lines
        if(char==' '):
            listBoard.append(currentLine)
            break
        #When a slash '/' is read (= every multiple of 9 char), a new list is created, which will contain the 
            #next line to add and the last read line is added to the list of lines
        if((i+1)%9==0):
            listBoard.append(currentLine)
            currentLine=[]
        #Adds the current char in the current list of char (= the current line)
        else:
            currentLine.append(char)
    return(listBoard)

def flipBlackPieces(listBoard):
    """
    Function that "flips" the positions of the black pieces to put them in their 
        corresponding place in the white player's side. This is necessary because the
        lists of values for each piece (in the beginning of this module) are only valid
        from the white player point of view (they are not symmetrical).
    Parameters :
        -listBoard : the current board (as a list of lists of strings)
    Returns :
        -listBoard : the current board but with the black positions flipped to be in their white correspondance
    """
    for i,line in enumerate(listBoard):
        for j,char in enumerate(line):
            #if there is only one char in the cell, we can "work" on it. Thus we don't work with the cells
                #where a black piece transposition has already been done.
            if(len(char)==1):
                #if the char is a lower case, it's a black piece
                if(char.islower()):
                    #The black piece is added to it's new position, and if there's a dash, it's
                        #replaced with an underscore 
                    listBoard[7-i][7-j]=listBoard[7-i][7-j].replace("-","_")+char
                    #The original cell of the black piece is filled by a single dash '-'
                    listBoard[i][j]='-'
    return listBoard

def getValueCell(cell,i,j):
    """
    Function that returns the value of the cell passed in parameter
    Parameters :
        -cell : the string contained in the cell
        -i : the position i of this cell
        -j : the position j of this cell
    Returns :
        -valueCell : the value of this cell, depending on the piece on it (if there is),
            the position of the cell, and the color of the piece (the value will be positive if
            it's a white piece, negative if it's a black piece)
            The values of each piece (10, 51, 32...) has been found on Internet
    """
    
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
    """
    Function that returns the total value of the board, by summing the value of each cell
    Parameters :
        -board : the current board, as a FEN string
    Returns :
        - the value of the current board, which is a float
            if it's positive, the white player's pieces have more value than the black ones
            if it's negative, the black player's pieces have more value than the white ones
    """
    listBoard=boardToArray(board.fen())
    reversedBlack=flipBlackPieces(listBoard)
    valueEval=0
    for i,line in enumerate(reversedBlack):
        for j,char in enumerate(line):
            valueEval+=getValueCell(reversedBlack[i][j],i,j)
    return valueEval
            
                    



