class MaxHeap:
    def __init__(self):
        self.heap = list()

    def percolate_up(self):
        n = len(self.heap)
        i = n-1

        while self.heap[(i-1)//2] < self.heap[i] and i > 0:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1) // 2

    def percolate_down(self):
        print(self.heap)
        n = len(self.heap)
        i = 0
        while True:
            if (2*i)+1 >= n:
                break
            else:
                pass
            left_child = self.heap[(2*i)+1]

            if (2*i)+2 >= n:
                right_child = -9999999999999999
            else:
                right_child = self.heap[(2*i)+2]

            print(f'i {i} root: {self.heap[i]} lc: {left_child} rc: {right_child}')
            if right_child > left_child and self.heap[i] < right_child:
                print('swapping with right')
                self.heap[i], self.heap[(2*i)+2] = self.heap[(2*i)+2], self.heap[i]
                i = (2*i)+2
            elif right_child < left_child and self.heap[i] < left_child:
                print('swapping with left')
                self.heap[i], self.heap[(2*i)+1] = self.heap[(2*i)+1], self.heap[i]
                i = (2*i)+1
            else:
                break


    def insert(self, val):
        self.heap.append(val)
        self.percolate_up()

    def get_max(self):
        return self.heap[0]

    def pop_max(self):
        n = len(self.heap)
        maxx = self.heap[0]
        self.heap[0], self.heap[n-1] = self.heap[n-1], self.heap[0]
        self.heap.pop()
        self.percolate_down()
        return maxx


if __name__ == '__main__':
    heap_obj = MaxHeap()
    heap_obj.insert(5)
    print(heap_obj.heap)
    heap_obj.insert(50)
    print(heap_obj.heap)
    heap_obj.insert(10)
    print(heap_obj.heap)
    heap_obj.insert(9)
    print(heap_obj.heap)
    heap_obj.insert(8)
    print(heap_obj.heap)
    heap_obj.insert(39)
    print(heap_obj.heap)
    heap_obj.insert(40)
    print(heap_obj.heap)
    heap_obj.pop_max()
    print(heap_obj.heap)
