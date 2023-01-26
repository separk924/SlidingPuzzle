import heapq, sys
from itertools import chain

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
            return None
        # if puzzle's width is even & the total number of inversions is even
        
        
    # add total number of inversions with the number of rows the gap is from the bottom
    totalInv += findGap(puzzle)
    
    # mod the total number of inversions
    totalInv = totalInv % 2
    
    # if puzzle's width is even, and total inversion sum is odd
    if totalInv != 0:
        return None
    
    # if puzzle's width is even, and total inversion sum is even
    
    return None

def aStar(puzzle):
    return None

def findGap(puz):
    gapPlace = 0
    for x in reversed(puz):
        if 0 in x:
            break
        gapPlace += 1
    return gapPlace

def main(argv):
    thePuz = './' + sys.argv[1]
    puzzle = open(thePuz, 'r')
    solve(puzzle.read())
    # print(puzzle.read())
    puzzle.close()
    
if __name__ == '__main__':
    main(sys.argv[1:])