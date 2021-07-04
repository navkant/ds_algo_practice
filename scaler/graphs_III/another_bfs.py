import queue
from heapq import heappop, heappush


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer

    def solve(self, A, B, C, D):
        adj_list = {}
        heap = []
        distance_array = []
        visit_array = [False for i in range(A)]

        for i in range(A):
            adj_list[i] = list()

        for edge in B:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        
        for k, v in adj_list.items():
            print(f"{k} | {v}")

        for i in range(A):
            if i != C:
                # heappush(heap, (float('inf'), i))
                distance_array.append(float('inf'))
            else:
                # heappush(heap, (0, i))
                heappush(heap, (0, i))
                distance_array.append(0)
            
        print(heap)
        print(distance_array)
        
        while len(heap):
            distance, xnode = heappop(heap)
            nbors = adj_list[xnode]
            visit_array[xnode] = True
            # print(f"{xnode} | {nbors}")
            for node, _distance in nbors:
                # print(f"    {node}, {distance}")
                if not visit_array[node]:
                    nbor_distance = distance + _distance
                    distance_array[node] = min(distance_array[node], nbor_distance)
                    heappush(heap, (nbor_distance, node))
                else:
                    pass
            # import pdb; pdb.set_trace()        
        print(f"print min distance is {distance_array[D]}")
        return distance_array[D]

if __name__ == "__main__":
    A = 7
    B = [[1, 5, 2],
        [5, 4, 2],
        [4, 6, 1],
        [1, 2, 1],
        [2, 3, 1],
        [3, 4, 1]]

    C = 1

    D = 6
    obj = Solution()
    obj.solve(A, B, C, D)
