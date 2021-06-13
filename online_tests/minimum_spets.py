def MinimumMoves(N):
    # this is default OUTPUT. You can change it.
    result = -404

    # write your Logic here:
    x = 1
    count = 1

    while True:
        if x * 2 >= N // 2:
            break
        x *= 2
        count += 1
    print(x, count)

    while (x + 1) * 2 <= N:
        x += 1
        count += 1

    x *= 2
    count += 1
    print(x, count)

    if x < N:
        for i in range(x, N):
            print(count, i)
            count += 1

    return count


if __name__ == '__main__':
    # INPUT [uncomment & modify if required]
    N = int(input())

    # OUTPUT [uncomment & modify if required]
    print(MinimumMoves(N))