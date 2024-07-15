class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        a=max(A)
        s=0
        e=M-1
        while e<=(len(A)-1):
            b=A[e]-A[s]
            if b<a:
                a=b
            s+=1
            e+=1
        return a
