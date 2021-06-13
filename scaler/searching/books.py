class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def student_required(self, arr, min_pages):
        n = len(arr)
        student_req = 1
        i = 0
        pages_read = 0

        while i < n:
            if arr[i] > min_pages:
                return -1
            pages_read += arr[i]
            if pages_read > min_pages:
                student_req += 1
                pages_read = 0
                continue
            else:
                pass
            i += 1

        return student_req

    def books(self, A, B):
        n = len(A)
        minn = A[0]
        maxx = A[0]
        pref_sum = [A[0]]

        for i in range(n):
            minn = min(minn, A[i])
            maxx = max(maxx, A[i])
            if i >= 1:
                pref_sum.append(pref_sum[i-1] + A[i])

        print(minn, maxx)

        start = pref_sum[0]
        end = pref_sum[-1]
        ans = end
        while start <= end:
            mid = start + (end - start) // 2

            req_student = self.student_required(A, mid)
            print(f'start {start} mid {mid} end {end} req {req_student}')
            if req_student == -1:
                start = mid + 1
            elif req_student == B:
                end = mid - 1
                ans = min(mid, ans)
            elif req_student < B:
                print('hola')
                end = mid - 1
                ans = min(mid, ans)
            else:
                start = mid + 1

        return ans


if __name__ == '__main__':
    a = [22]
    b = 1
    obj = Solution()
    ans = obj.books(a, b)
    print(f'ans is {ans}')
