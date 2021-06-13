import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # function to retrieve parent of given node
    def parent(self, pos):
        return pos // 2

    # function to retrieve left child of given node
    def left_child(self, pos):
        return (2 * pos)  # because tree indexing starts with 1 here otherwise it'd be (2*pos) + 1

    # function to retrieve right child of given node
    def right_child(self, pos):
        return (2 * pos) + 1  # because tree indexing starts with 1 here otherwise it'd be (2*pos) + 2

    # function that returns True if passed node is a leaf node
    def isLeaf(self, pos):
        if (pos >= self.size // 2) and pos <= self.size:
            return True
        return False

    # function to swap two nodes of heap
    def swap(self, fpos, spos, source=None):
        if source == 'Heapify':
            self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
        else:
            self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            l_child = self.Heap[self.left_child(pos)]
            r_child = self.Heap[self.right_child(pos)]
            if self.Heap[pos] < l_child or self.Heap[pos] < r_child:
                if l_child > r_child:
                    self.swap(pos, self.left_child(pos), 'Heapify')
                    self.maxHeapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos), 'Heapify')
                    self.maxHeapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def printTree(self):
        for i in range(1, (self.size // 2) + 1):
            print('Parent: ' + str(self.Heap[i]) +
                  'Left Child: ' + str(self.Heap[2 * i]) +
                  'Right Child: ' + str(self.Heap[2 * i + 1]))

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped


# Driver Code
if __name__ == "__main__":

    print('The maxHeap is ')

    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.printTree()
    max_value = maxHeap.extractMax()
    print("The Max val is " + str(max_value))
    maxHeap.printTree()
    max_value = maxHeap.extractMax()
    print("The Max val is " + str(max_value))
    maxHeap.printTree()
