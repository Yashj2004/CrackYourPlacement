class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=='{':
                a.append(s[i])
            elif len(a)==0 or s[i]==']' and a[len(a)-1]!='[' or s[i]==')' and a[len(a)-1]!='(' or s[i]=='}' and a[len(a)-1]!='{':
                return False
            else: 
                a.pop()
        if len(a)==0:
            return True
        else:
            return False
