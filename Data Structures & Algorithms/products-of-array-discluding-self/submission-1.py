class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        # prefix[i] = product of everything to the LEFT of i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # suffix[i] = product of everything to the RIGHT of i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = []
        for i in range(n):
            result.append(prefix[i] * suffix[i])

        return result