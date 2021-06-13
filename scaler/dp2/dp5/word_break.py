import sys
sys.setrecursionlimit(100000)

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer

    def __init__(self):
        self.hash_map = dict()

    def solve_word_break_dp(self, string, word_dict):
        n = len(string)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and string[j:i] in self.hash_map:
                    dp[i] = True
                else:
                    pass

        return dp[-1]


    def solve_word_break(self, string, start):
        print(f'string: {string} start: {start}')
        if start >= len(string):
            return True

        for end in range(start+1, len(string)+1):
            if string[start:end] in self.hash_map and self.solve_word_break(string, end):
                return True
        return False

    def wordBreak(self, A, B):
        for word in B:
            if word not in self.hash_map:
                self.hash_map[word] = 1
        print(self.hash_map)
        ans = self.solve_word_break(A, 0)
        print(f'recursive ans is {ans}')
        ans = self.solve_word_break_dp(A, B)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    A = "leetleetleethash"
    B = ["leet", "code", "hash"]
    obj = Solution()
    obj.wordBreak(A, B)