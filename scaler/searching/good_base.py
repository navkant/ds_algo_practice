class Solution:
    # @param A : string
    # @return a strings

    def get_good_number(self, number, base):
        length = 0
        one_count = 0

        while number:
            rem = number % base
            if rem != 1:
                pass
            else:
                one_count += 1

            length += 1
            number = number // base

        new_number = 0
        i = 0
        while i<length:
            new_number += base ** i
            i += 1

        return new_number, length

    def solve(self, A):
        low = 2
        high = int(A)-1
        B = int(A)
        
        low = 2
        high = 100

        while low <= high:
            mid = low + (high - low) // 2
            print(f'low {low} mid {mid} high {high}')
            good_no, length =  self.get_good_number(B, mid)
            print(f'good_no {good_no} length {length}')
            if good_no == B:
                return mid
            elif good_no < B:
                high = mid - 1
            else:
                low = mid + 1
            print()

        return B - 1


if __name__ == '__main__':
    a = 4831
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
