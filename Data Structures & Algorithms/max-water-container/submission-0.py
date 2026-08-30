class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left_i = 0
        right_i = len(heights) - 1
        size = []

        while left_i < right_i:
            temp_size = (right_i - left_i) * min(heights[left_i], heights[right_i])
            size.append(temp_size)
            
            if heights[left_i] < heights[right_i]:
                left_i += 1
            
            else:
                right_i -= 1
        
        return max(size)
            