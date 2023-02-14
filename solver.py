'''
This file contains the solve() function for the Sliding Puzzle. The solve()
function utilizes the A* algorithm to find the shortest path to the end state
for the puzzle which can look like this:
                                1   2   3   4
                                5   6   7   8
                                9   10  11 12
                                13  14  15  0
Author: Seung Park
Date: February 13, 2023
'''

########################################################################
# IMPORTS
########################################################################
import heapq, math, copy
from itertools import chain

'''
This class makes a constructor for the puzzle states
'''
class State():
    # constructor
    def __init__(self, prev=None, puz=None):
        self.g = 0
        self.h = 0
        self.f = 0
        self.prev = prev
        self.puzzle = puz
        self.move = None
        self.gapI = None
        self.gapJ = None
            
    # override the equality operator
    def __eq__(self, other):
        return self.puzzle == other.puzzle
    
    # override the comparison operator
    def __lt__(self, nxt):
        return self.f < nxt.f
    
    # override hash function
    def __hash__(self):
        thePuz = list(chain.from_iterable(self.puzzle))
        return hash((tuple(thePuz)))
    
'''
A function that takes a 2D array puzzle and finds the shortest path to
the goal state for the puzzle. This function returns a list of strings 
each of which is either 'U', 'D', 'L', or 'R', representing an “up”, “down”, 
“left”, or “right” move
'''
def solve(puzzle):
    # get width of puzzle
    width = len(puzzle[0])
            
    # flatten 2D list
    thePuz = list(chain.from_iterable(puzzle))
    
    # remove the 0
    thePuz.remove(0)
    
    # total number of inversions
    totalInv = 0
    for i in range(len(thePuz)):
        inversions = 0
        for j in range(len(thePuz)):
            # counts elements after a given element that are less than that element
            if thePuz[i] != thePuz[j] and thePuz[i] > thePuz[j] and i < j:
                inversions += 1
        totalInv += inversions
    
    # find whether width is odd or even
    width = width % 2
    totalInvMod = totalInv % 2
    
    if width != 0:
        # if puzzle's width is odd & the total number of inversions is odd, return unsolvable
        if totalInvMod != 0:
            print("line 41")
            return None
        # if puzzle's width is even & the total number of inversions is even
        return aStar(puzzle)
        
    # add total number of inversions with the number of rows the gap is from the bottom
    totalInv += findGap(puzzle)
    
    # mod the total number of inversions
    totalInv = totalInv % 2
    
    # if puzzle's width is even, and total inversion sum is odd
    if totalInv != 0:
        return None
    
    # if puzzle's width is even, and total inversion sum is even
    return aStar(puzzle)

'''
A function that takes a puzzle and finds a solution of minimum length,
returning a list of strings each of which is either 'U', 'D', 'L', or 
'R', representing an “up”, “down”, “left”, or “right” move
'''
def aStar(puzzle):
    # open and closed lists
    open = []
    closed = {} #should be a dictionary
    heapq.heapify(open)
    
    # get width and height of puzzle
    width = len(puzzle)
    height = len(puzzle[0])
    
    # initialize end state
    endState = [[0 for i in range(height)] for j in range(width)]
    
    # fill in the end state
    tile = 1
    for i, x in enumerate(endState):
        for j, y in enumerate(endState[0]):
            if i == width-1 and j == height-1:
                endState[i][j] = 0
            else:
                endState[i][j] = tile
            tile += 1
    
    # find the gap in the puzzle
    for i in range(width):
        for j in range(height):
            if puzzle[i][j] == 0:
                gapi = i
                gapj = j
                
    # create beginning and ending states
    start = State(None, puzzle)
    start.g = 0
    start.h = 0
    start.f = 0
    start.gapI = gapi
    start.gapJ = gapj
    end = State(None, endState)
    end.g = 0
    end.h = 0
    end.f = 0
    end.gapI = height
    end.gapJ = width
    
    # add start node to open list
    heapq.heappush(open, start)
    
    # continue searching while the open list is not empty
    while len(open) > 0:
        
        # take current state off open list and put on closed list
        current = heapq.heappop(open)
        closed.update({current : current.prev})
        
        # if current state is the goal state, return the path
        if current == end:
            paths = []
            curr = current
            while curr.prev is not None:
                paths.append(curr.move)
                curr = curr.prev
            return paths[::-1]
        
        ####### CREATE CHILDREN STATES ########
        
        # move tile down
        if current.gapI - 1 >= 0:
            moveTile(current, -1, 0, closed, open)
        
        # move tile up
        if current.gapI + 1 < width:
            moveTile(current, 1, 0, closed, open)
            
        # move tile right
        if current.gapJ - 1 >= 0:
            moveTile(current, 0, -1, closed, open)
            
        # move tile left
        if current.gapJ + 1 < height:
            moveTile(current, 0, 1, closed, open)

'''
A function that takes the current state, the indices of the changed tile 
position, the closed dictionary and open list and creates the children 
states of the current state
'''
def moveTile(curr, i, j, closed, open):
    newPuzzle = copy.deepcopy(curr.puzzle)
    newState = State(curr, newPuzzle)

    # move tile down & update state accordingly
    oldGap = curr.puzzle[curr.gapI][curr.gapJ]
    oldNum = curr.puzzle[curr.gapI+i][curr.gapJ+j]
    newState.puzzle[curr.gapI+i][curr.gapJ+j] = oldGap
    newState.puzzle[curr.gapI][curr.gapJ] = oldNum
    newState.g = curr.g + 1
    newState.h = heuristic(newState.puzzle)
    newState.f = newState.g + newState.h
    newState.gapI = curr.gapI+i
    newState.gapJ = curr.gapJ+j
    
    # update the move for the new state
    if i == -1:
        newState.move = 'D'
    if i == 1:
        newState.move = 'U'
    if j == -1:
        newState.move = 'R'
    if j == 1:
        newState.move = 'L'
    
    if newState not in closed.keys() and newState not in open:
        heapq.heappush(open, newState)

'''
A function that takes a puzzle as a 2D array and returns the total number
of moves left required to reach the goal state
'''
def heuristic(puzzle):
    # width of & height the puzzle
    width = len(puzzle[0])
    height = len(puzzle)
    
    # total moves away from goal state
    count = 0
    
    # iterate through puzzle to count the number of moves away from 
    # the goal state
    for i in range(height):
        for j in range(width):
            if puzzle[i][j] != 0:
                
                # get specific tile number
                num = puzzle[i][j]
                
                # get where tile's i position is located
                posI = math.floor((num - 1) / width)
                
                # get where tile's j position is located
                posJ = (num - 1) % width
                
                # add to total count of moves required
                count += abs(i - posI)
                count += abs(j - posJ)
                
    return count

'''
A function that takes in a puzzle and returns which row the gap is on
'''
def findGap(puz):
    gapPlace = 0
    for x in reversed(puz):
        if 0 in x:
            break
        gapPlace += 1
    return gapPlace