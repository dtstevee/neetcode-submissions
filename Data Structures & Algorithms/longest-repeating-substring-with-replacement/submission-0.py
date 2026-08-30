class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_depth = 0
        switch_num =k
        left_i = 0
        window_length = 0
        hash_map = {}
        
        for i,x in enumerate(s):
            if x in hash_map:
                hash_map[x] += 1
            else: 
                hash_map[x] = 1
            
            while (i - left_i + 1) - max(hash_map.values()) > k:
                hash_map[s[left_i]] -= 1
                left_i += 1
            
            max_depth = max(max_depth, (i - left_i + 1))
        
        return max_depth
            
                