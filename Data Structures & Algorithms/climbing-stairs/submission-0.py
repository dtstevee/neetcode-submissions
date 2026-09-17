class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp_0 = 1
        dp_1 = 1

        i = 2
        
        while i <= n:
            cur = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = cur
            i += 1
        
        return dp_1
