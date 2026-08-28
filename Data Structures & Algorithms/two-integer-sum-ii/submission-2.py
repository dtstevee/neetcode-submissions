class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_i = 0
        right_i = len(numbers) - 1
        result_list = []
        
        while left_i < right_i:
            left = numbers[left_i]
            right = numbers[right_i]
            temp_sum = left + right

            if temp_sum == target:
                return [left_i + 1, right_i + 1]

            elif temp_sum < target:
                left_i += 1
                continue
                
            else:
                right_i -= 1
                continue