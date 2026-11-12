class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer method
        left = 0
        longest = 0
        hashmap = set()
        
        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.remove(s[left])
                left += 1
            
            hashmap.add(s[right])
            longest = max(right - left + 1, longest)
        
        return longest