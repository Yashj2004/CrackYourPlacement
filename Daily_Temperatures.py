class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                s=st.pop()
                ans[s]=i-s
            st.append(i)
        return ans
