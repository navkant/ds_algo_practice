import sys

class Solution:
    def longest_inc_subsequence(self, arr):
        n = len(arr)
        dp = [-1] * N

        dp[0] = 1
        if arr[1] > arr[0]:
            dp[1] = 2
        else:
            dp[1] = 1
        
        print(dp)
        
        for i in range(2, n):
            dp[i] = 1

            for j in range(i):
                if arr[j] < arr[i] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]

        return max(dp)



if __name__ == "__main__":
    a = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
    N = len(a)
    obj = Solution()
    ans = obj.longest_inc_subsequence(a)
    print(f'ans is {ans}')