from heapq import heappop, heappush

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        ans = list()
        hp = list()
        heappush(hp, A)
        heappush(hp, B)
        heappush(hp, C)

        while len(ans) != D:
            ele = heappop(hp)
            ans.append(ele)
            heappush(hp, ele * A)
            heappush(hp, ele * B)
            heappush(hp, ele * B)

        print(ans)
        return ans


if __name__ == "__main__":
    A = 2
    B = 3
    C = 5
    D = 5
    obj = Solution()
    obj.solve(A, B, C, D)
