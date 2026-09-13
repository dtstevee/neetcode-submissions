class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # for this question, we aims to maintain a monotonic stack
        monotonic_stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
        
            while monotonic_stack and temperatures[i] > temperatures[monotonic_stack[-1]]:
                prev_i = monotonic_stack.pop()
                result[prev_i] = i - prev_i

            monotonic_stack.append(i)
        
        return result
                
                