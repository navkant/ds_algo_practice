class Soltion:
    def print_to_n(self, n):
        if n > 1:
            self.print_to_n(n-1)
        print(n, end=' ')

    def solve(self, n):
        self.print_to_n(n)

if __name__ == '__main__':
    a = 6
    obj = Soltion()
    obj.solve(a)
