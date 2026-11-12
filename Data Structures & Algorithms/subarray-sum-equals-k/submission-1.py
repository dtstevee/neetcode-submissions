class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create prefix, hashmap, and count
        prefix = 0
        count = 0
        hash_table = {0: 1}

        for i in nums:
            prefix += i
            
            count += hash_table.get(prefix - k, 0)
            
            hash_table[prefix] = hash_table.get(prefix, 0) + 1
        
        return count