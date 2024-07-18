class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        if strs is None or len(strs)==0:
            return ""
        minl=len(strs[0])
        for i in range (0,len(strs)):
            minl=min(minl,len(strs[i]))
        for i in range(0,minl):
            c=strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i]!=c:
                    return a
            a+=c
        return a
