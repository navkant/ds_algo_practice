from fractions import Fraction


def larget_number_array(arr):
    if len(arr) == 1:
        return arr[0]
    arr = sorted(arr)
    arr = list(map(str, arr))
    arr = sorted(A, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
    print('sorted ARRAY IS')
    print(arr)
    if len(arr) == 2:
        return max(int(''.join(arr)), int(''.join(arr[::-1])))

    ans = []
    while len(arr) > 2:
        print(f'l: {arr}')
        print(f'ans: {ans}')
        i = 0
        ans1 = int(''.join(ans + [arr[i]] + [arr[i + 1]]))
        ans2 = int(''.join(ans + [arr[i + 1]] + [arr[i]]))
        print(f'ans1: {ans1}')
        print(f'ans2: {ans2}')

        if ans1 > ans2:
            ans.extend([arr[i]])
            arr.remove(arr[i])
        else:
            ans.extend([arr[i + 1]])
            arr.remove(arr[i+1])

        if len(arr) == 2:
            print(f'arr: {arr}')
            print(f'ans: {ans}')
            ans1 = int(''.join(ans + [arr[i]] + [arr[i + 1]]))
            ans2 = int(''.join(ans + [arr[i + 1]] + [arr[i]]))
            if ans1 > ans2:
                ans.extend([arr[i], arr[i + 1]])
            else:
                ans.extend([arr[i + 1], arr[i]])
                arr.remove(arr[i])
            break
        # arr.remove(arr[i])
    return ''.join(ans)


def largestNumber(self, A):
    A = sorted(A, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
    print("SORTED ARRAY IS")
    print(A)
    i = 0
    while i < len(A)-1:
        if A[i] != 0:
            break
        else:
            i+=1
    ret = map(lambda x:str(x),A[i:])
    return ''.join(ret)


if __name__ == "__main__":
    a = [ 980, 674, 250, 359, 98, 969, 143, 379, 363, 106, 838, 923, 969, 880, 997, 664, 152, 329, 975, 377, 995, 943, 369, 515, 722, 302, 496, 124, 692, 993, 341, 785, 400, 113, 302, 563, 121, 230, 358, 911, 437, 438, 494, 599, 168, 866, 689, 444, 684, 365, 470, 176, 910, 204, 324, 657, 161, 884, 623, 814, 231, 694, 399, 126, 426 ]
    ans = larget_number_array(a)
    print('ans is : ', ans)