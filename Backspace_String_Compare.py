class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_st(word):
            a=[]
            for i in range(len(word)):
                a.append(word[i])
            ans=[]
            for i in range(len(a)):
                if a[i]=='#' and len(ans)>0:
                    ans.pop()
                elif a[i]=='#' and len(ans)<=0:
                    continue
                else:
                    ans.append(a[i])
            return "".join(ans)
        return build_st(s)==build_st(t)
