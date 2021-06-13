def lcs(str1, str2, m, n):
    if n == 0 or m == 0:
        return 0

    if str1[m-1] == str2[n-1]:
        x = 1 + max(lcs(str1, str2, m-1, n), lcs(str1, str2, m, n-1))
        return x
    else:
        # str1[m-1] != str2[n-1]
        return max(lcs(str1, str2, m, n-1), lcs(str1, str2, m-1, n))

if __name__ == '__main__':
    a1 = 'abcde'
    a2 = 'abfce'

    ans = lcs(a1, a2, len(a1), len(a2))
    print(ans)
