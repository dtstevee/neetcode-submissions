class Solution:
    def numDecodings(self, s: str) -> int:
        # define dp as the number of cut for previous state
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        i = 2

        while i <= len(s):
            dp[i] = 0
            
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
            i += 1
        
        return dp[-1]