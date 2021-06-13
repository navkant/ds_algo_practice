def solve(s, d, h, n):
    if n == 1:
        print(f'Moving disk {n} from {s} to {d}.')
        return
    solve(s, h, d, n - 1)
    print(f'Moving disk {n} from {s} to {d}.')
    solve(h, d, s, n - 1)

 
if __name__ == '__main__':
    solve('s', 'd', 'h', 3)
