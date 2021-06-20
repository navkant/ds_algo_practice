class Solution:

    def egg_drop_recursive(self, f, e):
        if f <= 1:
            return f
        
        if e == 1:
            return f
        
        ans = float('inf')
        for k in range(1, f):
            temp = 1 + max(self.egg_drop_recursive(k-1, e-1), self.egg_drop_recursive(f-k, e))
            ans = min(ans, temp)

        return ans

    def solve(self, floors, eggs):
        ans = self.egg_drop_recursive(floors, eggs)
        print(f"ans is: {ans}")


if __name__ == "__main__":
    obj = Solution()
    f = 14
    n = 3
    obj.solve(f, n)

