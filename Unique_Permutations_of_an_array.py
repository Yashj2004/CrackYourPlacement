class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        self.ans=[]
        d={}
        def backtrack(i,arr):
            if i==n:
                if not d.get(tuple(arr)):
                    self.ans.append(arr.copy())
                    d[tuple(arr)]=True
                return 
            for j in range(i,n):
                arr[i],arr[j]=arr[j],arr[i]
                backtrack(i+1,arr)
                arr[i],arr[j]=arr[j],arr[i]
        backtrack(0,arr)
        return sorted(self.ans)
                    

