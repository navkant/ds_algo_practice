""""""


def solve(ip, op):
    # print(f'IP: {ip}, OP: {op}')
    if len(ip) == 0:
        print(op)
        return
    first_char = ip[0]
    ip = ip[1:]
    try:
        int(first_char)
        solve(ip, op + first_char)
    except:
        solve(ip, op + first_char.lower())
        solve(ip, op + first_char.upper())


if __name__ == '__main__':
    string = 'a1B2'
    n = len(string)
    input = string
    output = ''
    solve(input, output)
