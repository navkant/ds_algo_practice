class Solution:
    def steps_to_climb_recursive(self, n):
        if n <= 2:
            return n

        return self.steps_to_climb_recursive(n-1) + self.steps_to_climb_recursive(n-2)

    def steps_to_climbs_iterative(self, n, second_last, last):
        if n <= 2:
            return n

        for i in range(3, n+1):
            temp = second_last
            second_last = last
            last = temp + second_last

        return last

    def solve(self, steps):
        ans = self.steps_to_climb_recursive(steps)
        print(f'recursive ans is {ans}')
        ans2 = self.steps_to_climbs_iterative(steps, 1, 2)
        print(f'iterative ans is {ans2}')


if __name__ == '__main__':
    a = 11
    obj = Solution()
    obj.solve(a)
