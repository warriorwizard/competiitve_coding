#User function Template for python3

class Solution:
    def knapSack(self,W, wt, val, n):
        final=0
        lis=[]
        for i in range(len(val)):
            lis.append(val[i]/wt[i])
        flag=True
        while flag==True:
            a=lis.index(max(lis))
            if wt[a]<=W:
                final+=wt[a]
                W-=wt[a]
                lis.pop(a)
                wt.pop(a)
                
            elif wt[a]>W:
                flag=False
        return final
       
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends