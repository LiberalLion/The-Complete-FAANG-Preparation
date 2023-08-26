class Solution:
    def MissingNumber(self,array,n):
        # code here
        total = n*(n+1)//2
        s = sum(array[i] for i in range(n-1))
        return total-s;

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
