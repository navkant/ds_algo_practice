# /*
#  * Given a string, find the longest substring which is palindrome.
#  */
#
# "aabc c bad"

# stack = []


def max_len_palindrome(string):
    n = len(string)
    stack = []

    max_length = 0
    ans = ""
    for i in range(n):
        if not stack:
            stack.append(string[i])
            continue

        elif len(stack) == 1 and stack[-1] == string[i]:
            j = len(stack) - 1
            k = i
            check_string = stack[-1] + string[i]
            length = len(check_string)
            if length > max_length:
                max_length = length
                ans = check_string

        elif len(stack) >= 2 and (stack[-1] == string[i] or stack[-2] == string[i]):
            print(stack)
            j = len(stack) - 1
            k = i
            check_string = ""
            flag = 0
            while (stack[j] == string[k] or stack[j-1] == string[k]):
                print(check_string)
                if stack[j] == string[k]:
                    check_string = stack[j] + check_string + string[k]
                    j -= 1
                    k += 1
                elif not flag:
                    check_string = stack[j]
                    j -= 1
                    flag = 1
                    continue
                else:
                    break
                if k == n or j == 0:
                    break

            print()
            length = len(check_string)
            if length > max_length:
                max_length = length
                ans = check_string
            else:
                pass
        stack.append(string[i])

    return ans


if __name__ == "__main__":
    # s = "bclevelllevel"
    s = 'aaaaa'
    # llevell
    ans = max_len_palindrome(s)
    print('ans is ', ans)
