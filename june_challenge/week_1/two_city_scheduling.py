class Solution:

    def knapsack(self, costs, N):
        if N == -1:
            return 0
        # print(costs[N])
        outcome1, outcome2 = costs[N][0] + self.knapsack(costs, N-1), costs[N][1] + self.knapsack(costs, N-1)
        # if self.a == len(costs)/2:
        #     return outcome2
        # elif self.b == len(costs)/2:
        #     return outcome1
        #
        # if outcome1 < outcome2:
        #     self.a += 1
        #     return outcome1
        # else:
        #     self.b += 1
        #     return outcome2
        return min(outcome1, outcome2)

    def twoCitySchedCost(self, costs) -> int:
        n = len(costs)
        ans = self.knapsack(costs, n-1)
        return ans


if __name__ == '__main__':
    sol = Solution()

    ans = sol.twoCitySchedCost([[10, 20], [30, 200], [400, 500], [30, 200]])
    print(ans)
