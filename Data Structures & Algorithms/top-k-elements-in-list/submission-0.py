class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        sorted_dict = sorted(hash_table.items(), key = lambda x: x[1],reverse = True)[:k]
        result = [x[0] for x in sorted_dict]
    
        return result