class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash_set = set()
        left_i = 0
        
        for i,x in enumerate(s):
            while x in hash_set:
                hash_set.remove(s[left_i])
                left_i += 1
                
            hash_set.add(x)
            max_length = max(max_length, len(hash_set))

        return max_length
                
                