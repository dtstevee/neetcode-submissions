class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[-1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        i=2

        while i < len(nums):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            i += 1
        
        return max(dp)