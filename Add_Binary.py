class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        carry=0
        i=len(a)-1
        j=len(b)-1
        while i>=0 or j>=0 or carry:
            s1=int(a[i]) if i>=0 else 0
            s2=int(b[j]) if j>=0 else 0
            sum=s1+s2+carry
            carry=sum//2
            rem=sum%2
            res.append(str(rem))
            i-=1
            j-=1
        return "".join(res[::-1])
