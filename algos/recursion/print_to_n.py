def print_to_n(n):
    if n == 0:
        return
    print(n, end=' ')
    print_to_n(n-1)
    # print(n, end=' ')


if __name__ == '__main__':
    n = 7
    print_to_n(n)
