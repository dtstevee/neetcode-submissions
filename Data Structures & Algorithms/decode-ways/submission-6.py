class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * len(s)
        dp[0] = 0 if s[0] == '0' else 1

        i = 1

        while i < len(s):
            dp[i] = 0

            # 当前数字自己用
            if s[i] != '0':
                dp[i] += dp[i-1]

            # 当前数字和前一个一起用
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]

            i += 1

        return dp[-1]