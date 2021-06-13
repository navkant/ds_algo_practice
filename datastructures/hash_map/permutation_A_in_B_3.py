class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def get_freq_map(self, string):
        freq_map = dict()

        for i in string:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map [i] += 1
        
        return freq_map

    def solve(self, A, B):
        substring_freq_map = self.get_freq_map(A)
        print('substring_freq_map: ', substring_freq_map)
        count = 0
        i = 0
        window_map = dict()
        while True:
            if i >= len(B):
                break

            if i < len(A):
                if B[i] not in window_map:
                    window_map[B[i]] = 1
                else:
                    window_map[B[i]] += 1
            else:
                if B[i] not in window_map:
                    window_map[B[i]] = 1
                else:
                    window_map[B[i]] += 1
                
                if B[i - len(A)] in window_map:
                    if window_map[B[i - len(A)]] == 1:
                        window_map.pop(B[i - len(A)])
                    else:
                        window_map[B[i - len(A)]] -= 1
            
            if window_map == substring_freq_map:
                count += 1
            i += 1
        return count

if __name__ == "__main__":
    A = "abc"
    A = A.lower()
    B = "abcbacabc"
    B = B.lower()
    obj = Solution()
    ans = obj.solve(A,B)
    print(ans)
