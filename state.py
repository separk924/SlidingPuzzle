import math
class State:
    def __init__(self, x, y, value, neighbors=None):
        self.value = value
        self.x = x
        self.y = y
        self.heuristic_value = -1
        self.distance_from_start = math.inf
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
            self.parent = None
            
    def __hash__(self):
        return hash((self.value, self.x, self.y, self.heuristic_value, self.distance_from_start))