class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas=sum(gas)
        sum_cost=sum(cost)
        if sum_gas<sum_cost:
            return -1
        cur=0
        s_index=0
        for i in range(len(gas)):
            cur+=gas[i]-cost[i]
            while cur<0:
                cur=0
                s_index=i+1
        return s_index
