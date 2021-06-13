class Solution:
    def __init__(self, arr_len, sum):
        self.t = []
        for i in range(arr_len + 1):
            row = [True]
            for j in range(sum):
                row.append(False)
            self.t.append(row)
        # for x in self.t:
        #     print(x)

    def subset_sum(self, wt_array, s, n):
        # print(f's: {s} n: {n} last element: {wt_array[n-1]}')
        for i in range(1, n+1):
            for j in range(1, s+1):
                if wt_array[i-1] <= j:
                    self.t[i][j] = self.t[i-1][j-wt_array[i-1]] or self.t[i-1][j]
                else:
                    self.t[i][j] = self.t[i-1][j]
        for x in self.t:
            print(x)
        return self.t[-1][-1]


if __name__ == '__main__':
    weight_array = [1, 3, 5, 8, 10]
    sum = 11
    obj = Solution(len(weight_array), sum)
    ans = obj.subset_sum(weight_array, sum, len(weight_array))
    print(ans)
