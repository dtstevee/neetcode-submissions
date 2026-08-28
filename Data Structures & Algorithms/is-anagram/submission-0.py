class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        for i, x in enumerate(s):
            if x in hashmap_s:
                hashmap_s[x] += 1
            else:
                hashmap_s[x] = 1
        
        for i, x in enumerate(t): 
            if x in hashmap_t:
                hashmap_t[x] += 1
            else:
                hashmap_t[x] = 1
        return hashmap_s == hashmap_t