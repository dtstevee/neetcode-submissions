class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_hash = {}
        for i in s1:
            if i in s1_hash:
                s1_hash[i] += 1
            else:
                s1_hash[i] = 1
        
        left = 0
        s2_hash = {}
        for right in range(len(s2)):
            # Add the value at right index to hashmap
            val = s2[right]
            if val in s2_hash:
                s2_hash[val] += 1
            else:
                s2_hash[val] = 1
            
            # if window size bigger than expected, we shift the left pointer and remove the left
            if (right - left + 1) > window_size:
                val_left = s2[left]
                s2_hash[val_left] -= 1
                if s2_hash[val_left] == 0:
                    del s2_hash[val_left]
                left += 1

            # at the solid window size, if match, return true
            if (right - left + 1) == window_size:
                if s1_hash == s2_hash:
                    return True
        return False                
            
        