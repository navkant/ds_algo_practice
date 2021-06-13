class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        min_element = 10 ** 7
        hash_map = dict()
        n = len(A)
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
            min_element = min(min_element, i)

        print(min_element)
        if min_element > 1:
            return 1
        min_element += 1

        while True:
            if min_element > 0 and min_element not in hash_map:
                break
            else:
                min_element += 1
        return min_element


if __name__ == '__main__':
    a = [894, 669, 852, 722, 778, 169, 247, 927, 875, 858, 396, 760, 318, 409, 640, 976, 419, 600, 711, 610, 864, 655, 859, 567, 7, 487, 953, 632, 544, 158, 53, 919, 45, 699, 493, 414, 586, 460, 339, 540, 12, 948, 515, 16, 116, 772, 529, 606, 684, 214, 724, 811, 925, 703, 454, 592, 330, 143, 41, 401, 570, 326, 885, 943, 836, 252, 119, 773, 768, 447, 581, 237, 380, 182, 457, 868, 667, 109, 702, 692, 542, 517, 966, 583, 983, 273, 641, 691, 985, 115, 574, 216, 372, 298, 411, 784, 95, 251, 389, 354, 964, 430, 991, 799, 824, 826, 714, 238, 967, 977, 291, 545, 355, 287, 425, 305, 118, 902, 479, 388, 19, 61, 301, 782, 688, 893, 673, 195, 971, 693, 797, 996, 3, 314, 353, 103, 391, 905, 316, 734, 54, 939, 648, 526, 448, 255, 690, 114, 715, 148, 376, 878, 483, 408, 804, 585, 79, 644, 621, 221, 345]
    obj = Solution()
    ans = obj.firstMissingPositive(a)
    print('ans is: ', ans)
