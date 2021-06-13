# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        m = len(A)
        array_list = []

        for i in range(m):
            x = TreeNode(A[i])
            array_list.append(x)

        for i in range(m):
            n = array_list[i]
            l = (2 * (i + 1)) - 1
            if l < m:
                n.left = array_list[l]
            else:
                pass

            r = (2 * (i + 1))
            if r < m:
                n.right = array_list[r]
            else:
                pass

        return array_list[0]




if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, 6, -1, -1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
