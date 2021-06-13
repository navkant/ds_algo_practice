"""Same as string_subsets.py just another method"""


def solve(ip, op):
    # print(f'IP: {ip}, OP: {op}')
    if len(ip) == 0:
        print(op, end=' ')
        return
    first_char = ip[0]
    ip1 = ip[1:]
    solve(ip1, op)
    op1 = op + first_char
    solve(ip1, op1)


if __name__ == '__main__':
    string = 'abc'
    n = len(string)
    input = string
    output = ''
    solve(string, output)
