class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        mod=1e9+7
        cnt=[0]*B
        for i in A:
            print(i%B)
            cnt[i%B]+=1
        print(cnt)
        ans=(cnt[0]*(cnt[0]-1))//2
        print(ans)
        i=1
        j=B-1
        while(i<=j):
            if(i==j):
                ans+=(cnt[i]*(cnt[j]-1))//2
                ans%=mod
            else:
                ans+=cnt[i]*cnt[j]
                ans%=mod
            i+=1
            j-=1
        return int(ans)


if __name__ == '__main__':
    a = [5, 17, 100, 11]
    print(a)
    obj = Solution()
    ans = obj.solve(a, 28)
    print('ans is ', ans)
