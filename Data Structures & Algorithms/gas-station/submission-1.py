class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        cur_gas = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            cur_gas += diff
            
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        
        if total_gas < 0:
            return -1
        else:
            return start


            
            