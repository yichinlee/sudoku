#################################################
# Hw5
# Your andrewID: yichinle
# Your section: Q
#################################################

#################################################
# Hw5 problems
#################################################

#### #1: COLLABORATIVE: removeRowAndCol ####
#Collaborators: (yixiaofu) 
import copy
#from class note
def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)
        
#loop thorugh rows to delete col
#create a newList to edit         
def nondestructiveRemoveRowAndCol(lst, row, col):
    newList = myDeepCopy(lst)
    del newList[row]
    for i in range(len(lst)-1):
        del newList[i][col]
    return newList
    
#directly edit on the lst
def destructiveRemoveRowAndCol(lst, row, col):
    del(lst[row])
    for i in range (len(lst)):
        del(lst[i][col])
    
#### #2: COLLABORATIVE: wordSearchWithWildcards(board, word) ####
#Collaborators: (list andrewIDs)
####################################
# customize these functions
####################################
# build on Word Search Animation from 09/27/18 Lecture
# Word Search Solver Algorithm
import string
def wordSearchWithWildcards(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            result = wordSearchFromPosition(board, word, row, col)
            if result != False:
                return result
    return False

def wordSearchFromPosition(board, word, row, col):
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if drow == dcol == 0:
                continue
            result = wordSearchFromPositionInDir(board, word, 
                                                    row, col, drow, dcol)
            if result != False:
                return result
    return False
#check the char of word in board in the same as word index 
def wordSearchFromPositionInDir(board, word, row, col, drow, dcol):
    curRow, curCol = row, col
    wordIndex = 0
    while wordIndex < len(word):
        if curRow < 0 or curRow >= len(board) or \
            curCol < 0 or curCol >= len(board[row]):
            return False
        #the item in board is an interger, skip the word index
        elif isinstance(board[curRow][curCol],int):
            num = board[curRow][curCol]
            if num == len(word)-wordIndex:
                return True
            elif num > len(word)-wordIndex:
                return False
            #update the current information
            else:
                wordIndex += num
                curRow += drow
                curCol += dcol
        elif board[curRow][curCol] != word[wordIndex] :
            return False
        else:
            curRow += drow
            curCol += dcol
            wordIndex += 1
    return True

####################################
# use the run function as-is
####################################

#### #3: Sudoku Logic ####
import math
def areLegalValues(values):
    #the lenth of the board should be N**2
    if len(values) == 0:
        return False
    if (len(values)**0.5)%1 == 0:
        for num in values:
            #the range of number in board should within then the size
            if isinstance(num,int) == False:
                return False
            if num > len(values) or num < 0:
                return False
            else:
                if num!=0:
                    if values.count(num)>1:
                        return False
        return True
    else:
        return False        

#check rows 
def isLegalRow(board, row):
    targetRow = board[row]
    if areLegalValues(targetRow):
        return True
    return False
        
#check cols
def isLegalCol(board, col):
    targetCol = []
    for i in range (len(board)):
        targetCol.append(board[i][col])
    if areLegalValues(targetCol):
        return True
    else:
        return False
#check block
def isLegalBlock(board, block):
    n = int(len(board)**0.5)
    targetBlock = []
    for row in range (block // n*n,block // n*n+n ):
        for col in range(block % n *n,block % n *n+n ):
            targetBlock.append(board[row][col])
    if areLegalValues(targetBlock):
        return True
    else:
        return False
    
#check everthing
def isLegalSudoku(board):
    for i in range(len(board)):
        if not isLegalRow(board,i):
            return False
        for j in range(len(board)):
            if not isLegalCol(board,j):
                return False
    for k in range (len(board)):
        if not isLegalBlock(board,k):
            return False
    return True

######################################################################
# GRAPHICS/ANIMATION PROBLEMS
# ignore_rest
# The autograder will ignore all code below here
# (But we won't!  This is where all tkinter problems go!)
######################################################################

from tkinter import *

#### #4: Sudoku Animation ####
def startBoard():
    #create a sudoku game board
    return [
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
            [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
            [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
            [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
            [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
            [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
            [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
            [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
            ]
            
def init(data):
    data.margin = 20
    data.board = startBoard()
    data.prefixBoard = startBoard()
    cellWidth = (data.width-data.margin)//len(data.board[0])
    cellHeight = (data.height-data.margin)//len(data.board)
    data.cellSize = min(cellWidth, cellHeight)
    #data.selected = []
    data.hightLightTop = 0
    data.hightLightLeft = 0
    data.N = len(data.board[0])**0.5
    data.size = (len(data.board[0]))
    data.highLightCurCol = 0
    data.highLightCurRow = 0
    data.keyInNum = 0
    data.win = 0
    
    
def drawBoard(canvas,data):
    #draw board, line and text
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            color = "systemTransparent"
            left = col*data.cellSize + data.margin/2
            top = row*data.cellSize + data.margin/2
            canvas.create_rectangle(left, top, 
                                    left + data.cellSize, top + data.cellSize,
                                    fill=color)
            
            bigLeft = (col//3)*3*data.cellSize + data.margin/2
            bigTop = (row//3)*3*data.cellSize + data.margin/2
            canvas.create_rectangle(bigLeft, bigTop, bigLeft + 3*data.cellSize, 
                                        bigTop + 3*data.cellSize, width = 3 )
            #draw text only if the board is legal
            if isLegalSudoku(data.board):
                if data.board[row][col] != 0:
                    canvas.create_text(left + data.cellSize/2, top + 
                                        data.cellSize/2,
                                        text=data.board[row][col],
                                        font="Arial " + 
                                        str(int(data.cellSize/2)) + " bold")
            else:
                data.board[data.highLightCurRow][data.highLightCurCol] == 0
                
#build on course note
def mousePressed(event, data):
    if data.win == 0:
        if data.margin/2 < event.y < data.height-data.margin/2 and \
        data.margin/2 < event.x < data.height-data.margin/2:
            data.highLightCurRow = int((event.y-data.margin/2) // data.cellSize)
            data.highLightCurCol = int((event.x-data.margin/2) // data.cellSize)
        
#high light the original numebr
def hightLightPrefixBoard(canvas,data):
    for row in range(len(data.prefixBoard)):
        for col in range(len(data.prefixBoard[row])):
            if data.prefixBoard[row][col] !=0:
                left = col*data.cellSize + data.margin/2
                top = row*data.cellSize + data.margin/2
                canvas.create_rectangle(left, top, left + data.cellSize, 
                                            top + data.cellSize, 
                                            fill="DarkSlateGray3")
#show "you win" when the game is over
def showWin(canvas,data):
    data.win = 1
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            if data.board[row][col] == 0:
                data.win = 0
    if data.win == 1:
        canvas.create_text(data.width/2, data.height/2,text = "YOU WIN", 
                            fill="red",font="Arial 40 bold" )

#highlight the current cell with yellow box
def highLight(canvas,data):
    data.hightLightLeft = (data.margin/2) + (data.highLightCurCol)*data.cellSize
    data.hightLightTop = (data.margin/2) + (data.highLightCurRow)*data.cellSize
    canvas.create_rectangle(data.hightLightLeft, data.hightLightTop, 
                            data.hightLightLeft + data.cellSize, 
                            data.hightLightTop + data.cellSize, fill="yellow")
                            
def keyPressed(event, data):
    #control hightlight square
    if data.win == 0:
        if event.keysym == "Up":
            if data.highLightCurRow - 1 < 0:
                data.highLightCurRow = data.size-1
            else:
                data.highLightCurRow -=1
        elif event.keysym == "Down":
            if data.highLightCurRow + 1 > (data.size-1):
                data.highLightCurRow = 0
            else:
                data.highLightCurRow +=1
        elif event.keysym == "Left":
            if data.highLightCurCol - 1 <0:
                data.highLightCurCol = (data.size-1)
            else:
                data.highLightCurCol -=1
        elif event.keysym == "Right":
            if data.highLightCurCol + 1 > (data.size-1):
                data.highLightCurCol = 0
            else:
                data.highLightCurCol +=1
        
        #type in number, also checking whether the board is legal
        if event.keysym in string.digits:
            data.keyInNum = event.keysym
            if data.board[data.highLightCurRow][data.highLightCurCol] == 0:
                data.board[data.highLightCurRow][data.highLightCurCol] = int(data.keyInNum)
                if not isLegalSudoku(data.board):
                    data.board[data.highLightCurRow][data.highLightCurCol] = 0
    
        #delete number            
        elif event.keysym == "BackSpace":
            #can not delete original number
            if data.prefixBoard[data.highLightCurRow][data.highLightCurCol] != 0:
                print("can not delete")
            else:
                data.board[data.highLightCurRow][data.highLightCurCol] = 0
                
#show view on the screen
def redrawAll(canvas, data):
    hightLightPrefixBoard(canvas,data)
    highLight(canvas,data)
    drawBoard(canvas,data)
    showWin(canvas,data)

def runSudoku(width=400, height=400):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
runSudoku()

#### Bonus: Sokoban Animation ####

def initSokoban(data):
    pass

def mousePressedSokoban(event, data):
    pass

def keyPressedSokoban(event, data):
    pass

def redrawAllSokoban(canvas, data):
    pass

def runSokoban(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllSokoban(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    initSokoban(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllSokoban(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

#################################################
# Hw5 Test Functions
# NOTE: starting this week, we will not provide any tests in the test functions.
# You need to write your own tests!
#################################################

def testNondestructiveRemoveRowAndCol():
    lst1 = [ [ 2, 3, 4, 5],
            [ 8, 7, 6, 5],
            [ 0, 1, 2, 3] ]
    result1 = [ [ 2, 3, 5],
            [ 0, 1, 3] ]
            
    lst2 = [[1,2,3,4]]*3
    result2 =  [ [ 1, 2, 4],
            [ 1, 2, 4] ]
    
    lst1Copy = copy.deepcopy(lst1)
    lst2Copy = copy.deepcopy(lst2)
    assert(nondestructiveRemoveRowAndCol(lst1, 1, 2) == result1)
    assert(lst1 == lst1Copy)
    assert(nondestructiveRemoveRowAndCol(lst2, 1, 2) == result2)
    assert(lst2 == lst2Copy)
    print("nondestructiveRemoveRowAndCol pass!")

def testDestructiveRemoveRowAndCol():
    lst1 = [ [ 2, 3, 4, 5],
            [ 8, 7, 6, 5],
            [ 0, 1, 2, 3] ]
    result1 = [ [ 2, 3, 5],
            [ 0, 1, 3] ]
            
    lst2 = [ ([1,2,3,4] * 1) for i in range(3) ]
    result2 =  [ [ 1, 2, 4],
            [ 1, 2, 4] ]
    assert(destructiveRemoveRowAndCol(lst1, 1, 2) == None)
    assert(destructiveRemoveRowAndCol(lst2, 1, 2) == None)
    assert(lst1 == result1)
    assert(lst2 == result2)
    print("destructiveRemoveRowAndCol pass!")

def testWordSearchWithWildcards():
    board1 = [ [ 'p', 'i', 'g' ],
            [ 's', 2, 'c' ],
            [ 'r', 7, 'd' ] ]
    board2 = [ ['o', 2, 'n', 2],
            ['a', 'g', 'a', 'r'],
            ['g', 'o', 'o', 'd'] ]
    board3 = [ ['a', 'r', 'k'],
            [ 3, 2, 'c'],
            ['e', 7, 'd'] ]
    assert(wordSearchWithWildcards(board1, "cows") == True)
    assert(wordSearchWithWildcards(board1, "cow") == True)
    assert(wordSearchWithWildcards(board1, "be") == True)
    assert(wordSearchWithWildcards(board1, "coowws") == False)
    assert(wordSearchWithWildcards(board2, "orange") == True)
    assert(wordSearchWithWildcards(board3, "apple") == True)
    assert(wordSearchWithWildcards(board3, "morning") == True)
    assert(wordSearchWithWildcards(board3, "mornnnning") == True)
    assert(wordSearchWithWildcards(board3, "goodluck") == False)
    print("wordSearchWithWildcards pass!")
    
def testAreLegalValues():
    assert(areLegalValues([]) == False)
    assert(areLegalValues([None, 2, None, 4, 5, None, 7, 8, 9])== False)
    assert(areLegalValues([ 5, 3, 0, 0, 7, 0, 0, 0, 0 ]) == True)
    assert(areLegalValues([ 5, 3, 3, 0, 7, 7, 7, 0, 0 ]) == False)
    print("areLegalValues pass!")

def createTestBoard():
    return [
            [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
def createTestBoard2():
    return [[4, 0, 0, 0], [0, 3, 0, 0], [3, 2, 1, 0], [0, 0, 4, 2]]
    
def createErrorTestBoard():
    return [
            [ 5, 3, 3, 0, 7, 0, 0, 0, 0 ],
            [ 6, 60, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 8, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 4, 0, 8, 0, 3, 40, 0, 1 ],
            [ 7, 7, 6, 0, 2, 3, 0, 0, 6 ],
            [ 0, 6, 6, 0, 0, 0, 2, 8, 0 ],
            [ 0, 1, 1, 4, 1, 9, 0, 2, 5 ],
            [ 0, 55, 0, 0, 8, 0, 0, 7, 2 ]
            ]

def testIsLegalRow():
    assert(isLegalRow(createTestBoard(),1) == True)
    assert(isLegalRow(createErrorTestBoard(),1) == False)
    print("isLegalRow pass!")

def testIsLegalCol():
    assert(isLegalCol(createTestBoard(),1) == True)
    assert(isLegalCol(createErrorTestBoard(),2) == False)
    print("isLegalCol pass!")

def testIsLegalBlock():
    assert(isLegalBlock(createTestBoard(),1) == True)
    assert(isLegalBlock(createErrorTestBoard(),8) == False)
    print("isLegalBlock pass!")

def testIsLegalSudoku():
    assert(isLegalBlock(createTestBoard2(),1) == True) 
    assert(isLegalBlock(createTestBoard(),5) == True)
    assert(isLegalBlock(createErrorTestBoard(),5) == False)
    print("isLegalSudoku pass!")

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testSokobanAnimation():
    print("Running Sokoban Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSokoban(width, height)
    print("Done!")

#################################################
# Hw5 Main
#################################################

def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testWordSearchWithWildcards()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSudokuAnimation()
    #testSokobanAnimation() # this is bonus- un-comment if you want to try!

def main():
    testAll()

if __name__ == '__main__':
    main()