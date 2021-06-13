"""Same as string_subsets.py just another method"""


def solve(ip, op):
    # print(f'IP: {ip}, OP: {op}')
    if len(ip) == 0:
        print(op)
        return
    first_char = ip[0]
    ip = ip[1:]
    solve(ip, op + first_char)
    solve(ip, op + ' ' + first_char)


if __name__ == '__main__':
    string = 'abcd'
    n = len(string)
    input = string
    first_c = input[0]
    # print(first_c)
    input = input[1:]
    output = first_c
    solve(input, output)
