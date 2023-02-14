########################################################################
# IMPORTS
########################################################################
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