class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        stack=[]
        for i in range(len(S)):
            if S[i].isdigit():
                stack.append(S[i])
            if S[i]=='+':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)+int(b))
            elif S[i]=='-':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)-int(b))
            elif S[i]=='*':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)*int(b))
            elif S[i]=='/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)//int(b))
        return stack[-1]
