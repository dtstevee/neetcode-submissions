class Solution:
    def findMaxConsecutiveOnes(self, nums):
        temp_result = 0
        result = 0

        for i in range(len(nums)):
            fir = nums[i]

            if fir == 1:
                temp_result += 1

                if temp_result > result:
                    result = temp_result
            else:
                temp_result = 0

        return result