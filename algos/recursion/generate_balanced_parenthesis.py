def solve(open, close, output, v):
    # print(f'open: {open}, close: {close}, output: {output}')
    # print(f'v: {v}')
    if open == 0 and close == 0:
        v.append(output)
        return
    if open != 0:
        # open = open - 1
        op1 = output + '('
        solve(open-1, close, op1, v)
    if close > open:
        op3 = output + ')'
        solve(open, close-1, op3, v)
    # return v


if __name__ == '__main__':
    n = 4
    open = n
    close = n
    o = ''
    ans_list = list()
    solve(open, close, o, ans_list)
    print(ans_list)
