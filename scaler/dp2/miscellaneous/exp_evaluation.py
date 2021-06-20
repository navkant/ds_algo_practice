class Solution:
    def exp_eval_recursive(self, expression, i, j, is_true):
        # print(f'i: {i}, j: {j}')
        if i > j:
            return 0
        if i == j:
            if is_true:
                if expression[i] == 'T':
                    return 1
                else:
                    return 0
            else:
                if expression[i] == 'F':
                    return 1
                else:
                    return 0

        ans = 0
        for k in range(i+1, j, 2):
            # print(f'  k:{k}')
            lt = self.exp_eval_recursive(expression, i, k-1, True)
            lf = self.exp_eval_recursive(expression, i, k-1, False)
            rt = self.exp_eval_recursive(expression, k+1, j, True)
            rf = self.exp_eval_recursive(expression, k+1, j, False)

            if expression[k] == '&':
                if is_true:
                    ans += lt * rt
                else:
                    ans += (lf * rt) + (lt * rf) + (lf * rf)
            elif expression[k] == '|':
                if is_true:
                    ans += (lt * rt) + (lt * rf) + (lf * rt)
                else:
                    ans += (lf * rf)
            elif expression[k] == '^':
                if is_true:
                    ans += (lf * rt) + (lt * rf)
                else:
                    ans += (lf * rf) + (lt * rt)

        return ans

    def exp_eval_dp(self, expression, i, j, is_true, dp):
        print(f'i: {i}, j: {j}')
        if i > j:
            return False
        if i == j:
            if is_true:
                if expression[i] == 'T':
                    return 1
                else:
                    return 0
            else:
                if expression[i] == 'F':
                    return 1
                else:
                    return 0

        if is_true:
            if dp[i][j]['True'] != -1:
                return dp[i][j]['True']
            else:
                pass
        else:
            if dp[i][j]['False'] != -1:
                return dp[i][j]['False']
            else:
                pass

        ans = 0
        for k in range(i+1, j, 2):
            print(f'  k:{k}')
            lt = self.exp_eval_recursive(expression, i, k-1, True)
            lf = self.exp_eval_recursive(expression, i, k-1, False)
            rt = self.exp_eval_recursive(expression, k+1, j, True)
            rf = self.exp_eval_recursive(expression, k+1, j, False)

            if expression[k] == '&':
                if is_true:
                    ans += lt * rt
                else:
                    ans += (lf * rt) + (lt * rf) + (lf * rf)
            elif expression[k] == '|':
                if is_true:
                    ans += (lt * rt) + (lt * rf) + (lf * rt)
                else:
                    ans += (lf * rf)
            elif expression[k] == '^':
                if is_true:
                    ans += (lf * rt) + (lt * rf)
                else:
                    ans += (lf * rf) + (lt * rt)

        if is_true:
            dp[i][j]['True'] = ans
        else:
            dp[i][j]['False'] = ans

        return ans

    def solve(self, expr):
        n = len(expr)
        ans = self.exp_eval_recursive(expr, 0, n-1, True)
        print(f'ans is {ans}')
        dp = [[{'True': -1, 'False': -1} for i in range(n)] for j in range(n)]
        ans2 = self.exp_eval_dp(expr, 0, n-1, True, dp)
        print()
        for row in dp:
            print(row)
        print(f'Iterative ans is {ans2}')



if __name__ == '__main__':
    a = "T^F^T|T"
    obj = Solution()
    obj.solve(a)