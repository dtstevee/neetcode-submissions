class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list_len = len(s1)
        s1_hash = {}
        for i in s1:
            if i in s1_hash:
                s1_hash[i] += 1
            else:
                s1_hash[i] = 1
        
        left_i = 0
        right_i = list_len

        while right_i - 1 <= len(s2):
            temp_hash = {}
            list_range = s2[left_i:right_i]

            for i in list_range:
                if i in temp_hash:
                    temp_hash[i] += 1
                else:
                    temp_hash[i] = 1
            
            if temp_hash == s1_hash:
                return True
            else:
                left_i += 1
                right_i += 1
        
        return False

