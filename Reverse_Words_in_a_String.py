class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        s=s[::-1]
        a=""
        print(s)
        for i in range(len(s)):
            if s[i]!='':
                a+=s[i]
                a+=" "
        return a[:-1]
