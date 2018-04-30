# seven queens, recursive
from typing import List
import Draw

#if position for queen hasn't already been selected, return True
def noDupes(q, currentQueen):
    return q[currentQueen] not in q[0: currentQueen]

#checks if queen has been inserted on a diagonal, if a clash return False
def noDiagonalClash(q, currentQueen):
    for col in range(currentQueen):
        if currentQueen - col == abs(q[currentQueen] - q[col]): return False
    return True
    
#if there are no duplicate queens or diagonal queens, new position is deemed OK
def isOK(q, currentQueen):  
    return noDupes(q, currentQueen) and noDiagonalClash(q, currentQueen)

#initialize global variable for solution number
countSolutions = 0

#recursively determines where the queens should be placed
def solveQueens(q, currentQueen):
    global countSolutions
    if currentQueen == 7:
        countSolutions += 1
        #resets game board
        gameBoard()
        #shows solution of 7 queens
        for i in range(7):
            queen(i, q[i])
            
        #prints all soultions   
        print("solution: ", countSolutions, "is", q)
        return q
    
    for i in range(7):
        #slows down the computation so the board stays for a few seconds
        Draw.show(20)
        
        #try to place the queen
        q[currentQueen] = i
        if isOK(q, currentQueen): solveQueens(q, currentQueen+1)
                          
#creates game background            
def gameBoard():
    Draw.picture("checkerboard.gif", 0, 0)

#creates representation of a queen    
def queen(x, y):
    Draw.setColor(Draw.RED)
    Draw.filledRect((x*40)+7, y*40, 30, 30)
    
def __main():
    #Draw starting position of the board
    Draw.setCanvasSize(275, 260)
    gameBoard()
    
    #initialize solve queens algorithm
    q = [0] * 7
    print(solveQueens(q, 0))
    
    
if __name__ == '__main__':
    __main() 