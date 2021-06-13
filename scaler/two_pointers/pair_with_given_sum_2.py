class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 10**9 + 7
        u_elements = []
        freq_map = {}

        for i in A:
            if i not in freq_map:
                freq_map[i] = 1
                u_elements.append(i)
            else:
                freq_map[i] += 1


        n = len(u_elements)
        i = 0
        j = n - 1
        count = 0
        print(u_elements)
        print(freq_map)
        if len(u_elements) == 1 and freq_map[u_elements[0]] > 1 and ((B % u_elements[0]) == 0):
            freq = freq_map[u_elements[0]]
            return (freq * (freq-1))//2

        while i < j:
            if B/2 == u_elements[i] and freq_map[u_elements[i]] > 1:
                freq = freq_map[u_elements[i]]
                count += (freq * (freq-1))//2
            elif B/2 == u_elements[j] and freq_map[u_elements[j]] > 1:
                freq = freq_map[u_elements[j]]
                count += (freq * (freq-1))//2

            summ = u_elements[i] + u_elements[j]
            print(f'i: {i} j: {j} sum: {summ}')
            if summ > B:
                j -= 1
            elif summ < B:
                i += 1
            elif summ == B:
                count1 = freq_map[u_elements[i]]
                print('c1', count1)
                count2 = freq_map[u_elements[j]]
                print('c2', count2)
                print('contri ', count1 * count2)
                count += count1 * count2
                j -= 1

        return count



if __name__ == '__main__':
    a = [ 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666, 4629666]
    b = 9259332
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
