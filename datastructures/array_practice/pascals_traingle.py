class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        array = [[1], [1, 1]]
        a =  1
        for i in range(2, A):
            row = list()
            for j in range(i):
                if i == 0 and j == 0:
                    row.append(1)
                elif i != 0 and j == 0:
                    row.append(array[i-1][0])
                elif i != 0 and j!= 0:
                    row.append(array[i-1][j-1] + array[i-1][j])
            row.append(1)
            array.append(row)
        return array


if __name__ == "__main__":
    a = 5
    
    obj = Solution()
    ans = obj.solve(a)
    for i in ans:
        print(i)
