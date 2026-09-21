class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        def house_robber(nums):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 0:
                return 0
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            i = 2
            
            while i < len(dp):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                i += 1
            return max(dp)
        list_1 = nums[:-1]
        list_2 = nums[1:]
        return max(house_robber(list_1), house_robber(list_2))
