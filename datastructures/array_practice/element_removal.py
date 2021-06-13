class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        # print('sorted array is: ', A)
        removal_cost = 0
        for i in range(len(A)-1, -1, -1):
            cost = 0
            for j in range(i+1):
                cost += A[j]
            removal_cost += cost
        # print('removal cost is: ', removal_cost)

        return removal_cost


if __name__ == "__main__":
    a = [8, 0, 10]
    obj =  Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
