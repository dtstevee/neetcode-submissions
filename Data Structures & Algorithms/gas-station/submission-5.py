class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_travel = 0
        cur_gas = 0
        start = 0

        for i in range(len(gas)):
            cur_cost = gas[i] - cost[i]
            cur_gas += cur_cost
            total_travel += cur_cost
            
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        if total_travel < 0:
            return -1
        
        return start