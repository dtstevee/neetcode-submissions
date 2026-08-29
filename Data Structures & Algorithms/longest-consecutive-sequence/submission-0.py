class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        non_duplicate = set(nums)
        max_depth = 0


        for i in nums:
            last_num = i - 1
            if last_num not in non_duplicate:
                current = i
                depth = 1

                while current + 1 in non_duplicate:
                    current += 1
                    depth += 1
                
                if max_depth < depth:
                    max_depth = depth
        return max_depth
                