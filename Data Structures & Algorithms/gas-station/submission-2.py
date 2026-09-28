class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        cur_gas = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            cur_gas += diff
            
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        

        return start


            
            