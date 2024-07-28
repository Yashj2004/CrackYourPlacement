class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        stack=[]
        while i<len(tokens): 
            if tokens[i]=='+':
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif tokens[i]=='-':
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif tokens[i]=='*':
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif tokens[i]=='/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(tokens[i]))
            i+=1
        return stack[-1]

