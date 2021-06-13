class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        choclates = 0
        n = len(B)
        total_choclates = 0
        prefix_sum = [0] * n
        prefix_sum[0] = B[0]
        for i in range(1, n):
            if B[i] > B[i-1]:
                prefix_sum[i] = prefix_sum[i-1] + B[i]
            else:
                prefix_sum[i] = B[i]

        return max(prefix_sum)

if __name__ == '__main__':
    a = [167, 96, 583, 563, 250, 128, 601, 33, 560, 326, 755, 537, 609, 931, 447, 26, 759, 144, 660, 866, 257, 825, 743, 936, 453, 926, 891, 53, 71, 9, 437, 761, 144, 266, 616, 444, 897, 973, 132, 450, 837, 590, 602, 5, 408, 898, 548, 34, 282, 412, 821, 748, 706, 330, 882, 60, 72, 76, 894, 297, 854, 868, 460, 743, 224, 562, 646, 841, 809, 262, 505, 173, 722, 99, 38, 22, 783, 517, 631, 366, 561, 219, 494, 447, 182, 917, 276, 714, 759, 727, 391, 811, 300, 84, 833, 40, 48, 615, 616, 216]
    print(a)
    obj = Solution()
    ans = obj.solve(0, a)
    print('ans is: ', ans)
