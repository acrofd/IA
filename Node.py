class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
       if self.f < other.f :
            return  -1