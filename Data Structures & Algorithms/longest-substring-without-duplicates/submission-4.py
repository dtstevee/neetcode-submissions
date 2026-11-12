class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        from collections import deque
        longest_length = 0
        slide_w = deque()
        hashmap = set()
        
        for item in s:

            while item in hashmap:
                removed = slide_w.popleft()
                hashmap.remove(removed)

            slide_w.append(item)
            hashmap.add(item)

            longest_length = max(longest_length, len(slide_w))

        return longest_length