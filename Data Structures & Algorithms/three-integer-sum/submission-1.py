class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        result_list = []
        
        for i,x in enumerate(sorted_list):
            if i > 0 and x == sorted_list[i - 1]:
                continue
            target =  -x
            left_i = i + 1
            right_i = len(sorted_list) - 1

            while left_i < right_i:
                left = sorted_list[left_i]
                right = sorted_list[right_i]
                temp_sum = left + right

                if temp_sum == target:
                    result_list.append([x, left, right])
                    left_i += 1
                    right_i -= 1
                    while (left_i < right_i and sorted_list[left_i]== sorted_list[left_i -1]):
                        left_i += 1

                elif temp_sum < target:
                    left_i += 1


                else:
                    right_i -= 1

        
        return result_list
            
                    