class Solution:
    def __init__(self):
        pass

    def two_minimum(self, array):
        min1 = 10**7
        min2 = 10**7
        n = len(array)
        for i in range(n):
            if array[i] < min1:
                min1 = array[i]

        for i in range(n):
            if array[i] == min1:
                continue
            else:
                if array[i] < min2:
                    min2 = array[i]
        print(f'min1: {min1} min2: {min2}')


if __name__ == '__main__':
    a = [3, 5, 4, 10, 7, 9]
    print(a)
    obj = Solution()
    obj.solve(a)
