# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def __init__(self):
        self.in_map = {}
        self.pre_map = {}

    def construct_tree(self, A, B, li_in, ri_in, li_pre, ri_pre):
        # print(f'li_in: {li_in}, ri_in: {ri_in} li_pre: {li_pre} ri_pre: {ri_pre}')
        if li_in > ri_in:
            return None

        print(f'{ri_in - li_in} , {ri_pre - li_pre}')

        value = A[li_pre]
        print(f'li_pre: {li_pre} value: {value}')
        root = TreeNode(value)

        root.left = self.construct_tree(A, B, li_in, self.in_map[value]-1, li_pre+1, li_pre + self.in_map[value]-li_in)
        if self.in_map[value] + 1 >= len(A):
            root.right = None
        else:
            root.right = self.construct_tree(A, B, self.in_map[value]+1, ri_in, li_pre + self.in_map[value]-li_in + 1, ri_pre)

        return root

    def buildTree(self, A, B):
        for i in range(len(A)):
            if A[i] not in self.pre_map:
                self.pre_map[A[i]] = i

        for i in range(len(B)):
            if B[i] not in self.in_map:
                self.in_map[B[i]] = i

        return self.construct_tree(A, B, 0, len(B)-1, 0, len(A)-1)



if __name__ == '__main__':
    a = [1000, 200]  # pre order
    b = [200, 1000]  # in order
    obj = Solution()
    ans = obj.buildTree(a, b)
    print(f'ans is {ans}')
    obj.preorder_traversal(ans)
    ans2 = obj.check_sum(ans, 0, 57)
    print(f'ans is {ans2}')
