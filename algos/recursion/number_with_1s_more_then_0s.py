def solve(output, one_count, zero_count, n):
    if n == 0:
        print(output)
        return
    if one_count > zero_count:
        op1 = output + '0'
        solve(op1, one_count, zero_count+1, n-1)
        op2 = output + '1'
        solve(op2, one_count+1, zero_count, n - 1)
    else:
        op3 = output + '1'
        solve(op3, one_count+1, zero_count, n-1)


if __name__ == '__main__':
    N = 5
    op = ''
    one_cnt = 0
    zero_cnt = 0
    solve(op, one_cnt, zero_cnt, N)
