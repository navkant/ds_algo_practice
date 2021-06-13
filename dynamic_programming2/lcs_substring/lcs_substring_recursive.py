def lcs_substring(str1, str2, m, n, count):
    if n == 0 or m == 0:
        return count

    if str1[m-1] == str2[n-1]:
        count = lcs_substring(str1, str2, m-1, n-1, count+1)
   
    count = max(count, max(lcs_substring(str1, str2, m-1, n, 0), lcs_substring(str1, str2, m, n-1, 0)))
    return count


if __name__ == '__main__':
    a1 = 'faui'
    a2 = 'fabe'

    ans = lcs_substring(a1, a2, len(a1), len(a2), 0)
    print(ans)