class Solution:
    # @param A : tuple of strings
    # @return an integer
    # function to check all boxes
    def check_boxes(self, A):
        x = 0
        y = 0
        bottom = 3
        right = 3
        while True:
            d = dict()
            for i in range(x, bottom):
                for j in range(y, right):
                    if A[i][j] == '.':
                        continue
                    if A[i][j] not in d:
                        d[A[i][j]] = 1
                    else:
                        return 0
            if j == len(A) - 1:
                x += 3
                y = 0
                bottom += 3
                right = 3
            else:
                y += 3
                right += 3
            if i == (len(A) - 1) and j == (len(A) - 1):
                break
        return 1
    
    def isValidSudoku(self, A):
        # checking all rows
        for i in A:
            d = {}
            for j in i:
                if j == '.':
                    continue
                else:
                    if j not in d:
                        d[j] = 1
                    else:
                        return 0

        # checking all columns
        i = 0
        j = 0
        for j in range(len(A)):
            d = {}
            for i in range((len(A))):
                if A[i][j] == '.':
                    continue
                else:
                    if A[i][j] not in d:
                        d[A[i][j]] = 1
                    else:
                        return 0
                       
        #checking all boxes
        return self.check_boxes(A)


if __name__ == "__main__":
    a = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
    obj = Solution()
    ans = obj.isValidSudoku(a)
    print(ans)