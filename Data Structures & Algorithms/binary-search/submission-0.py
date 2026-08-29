class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left)//2
            temp_target = nums[mid]
            
            if temp_target == target:
                return mid
            
            elif temp_target < target:
                left = mid + 1
            
            
            else:
                right = mid - 1

        return -1
