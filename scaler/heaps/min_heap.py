class MinHeap:
    def __init__(self):
        self.heap = list()

    def percolate_up(self):
        n = len(self.heap)
        i = n-1

        while self.heap[(i-1)//2] > self.heap[i] and i > 0:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1) // 2

    def percolate_down(self):
        n = len(self.heap)
        i = 0
        while True:
            if (2*i)+1 >= n:
                break

            else:
                pass
            left_child = self.heap[(2*i)+1]

            if (2*i)+2 >= n:
                right_child = 9999999999999999
            else:
                right_child = self.heap[(2*i)+2]

            if right_child < left_child and self.heap[i] > right_child:
                self.heap[i], self.heap[(2*i)+2] = self.heap[(2*i)+2], self.heap[i]
                i = (2*i)+2
            elif right_child > left_child and self.heap[i] > left_child:
                self.heap[i], self.heap[(2*i)+1] = self.heap[(2*i)+1], self.heap[i]
                i = (2*i)+1
            elif right_child == left_child and self.heap[i] > left_child:
                self.heap[i], self.heap[(2*i)+1] = self.heap[(2*i)+1], self.heap[i]
                i = (2*i)+1
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.percolate_up()

    def get_min(self):
        return self.heap[0]

    def pop_min(self):
        n = len(self.heap)
        maxx = self.heap[0]
        self.heap[0], self.heap[n-1] = self.heap[n-1], self.heap[0]
        self.heap.pop()
        self.percolate_down()
        return maxx


if __name__ == '__main__':
    heap_obj = MinHeap()
    a = [93, 23, -38, 70, -24, -25, -84, 34, 30, 9, -68, 80, 8, -65, 22, -68, -20, -74, 83, -65, 39, 67, -30, -96, -63, 26, 63, 33, -99, -93, 34, 71, -45, -25, 82, 64, -27, -67, 76, 88, 15, -54, 25, 39, -81, -92, 13, -88, -99, 39, -72, -35, 66, 67, -82, 99, 93, -40, 42, -45, -24, -27, -67, 12, -60, 60, 96, -70, 6, 13, -3, -62, -50, 95, -68, 28, -65, -48, -25, 62]
    b = 15782
    for i in a:
        heap_obj.insert(i)
    print(f'Heap: {heap_obj.heap}')
    print('Sorting....')
    for i in range(b):
        heap_obj.insert((-1) * heap_obj.pop_min())
        print(heap_obj.heap)

    print(heap_obj.heap)
    print(sum(heap_obj.heap))
