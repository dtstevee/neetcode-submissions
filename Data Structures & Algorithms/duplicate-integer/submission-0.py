class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashset

        seen = set()
        
        for i,x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
        return False