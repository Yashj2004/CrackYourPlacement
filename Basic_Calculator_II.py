class Solution:
    def calculate(self, s: str) -> int:
        i=0
        cur=0
        prev=0
        res=0
        current_operation='+'

        while i<len(s):
            cur_char=s[i]

            if cur_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur=cur*10+int(s[i])
                    i+=1
                i-=1

                if current_operation=='+':
                    res+=cur
                    prev=cur

                elif current_operation=='-':
                    res-=cur
                    prev=-cur

                elif current_operation=='*':
                    res-=prev
                    res+=(prev*cur)
                    prev=(prev*cur)

                else:
                    res-=prev
                    res+=int(prev/cur)
                    prev=int(prev/cur)
                cur=0
            elif cur_char!=' ':
                current_operation=cur_char
            i+=1
        return res
