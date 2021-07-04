class CoordsToNode:
    # @param A : list of list of integers
    # @return a list of list of integers
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_node(self, i, j, zero_based=True):
        if i >= self.height or j >= self.width:
            return "coords out of matrix"
        if zero_based:
            node = (i * self.width) + j
        else:
            node = (i * self.width) + (j+1)

        return node

