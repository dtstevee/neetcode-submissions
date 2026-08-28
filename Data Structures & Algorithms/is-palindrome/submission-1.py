class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_char = ''
        for i in s:
            if i.isalnum():
                clean_char += i.lower()

        left_i = 0
        right_i = len(clean_char) - 1
        
        while left_i < right_i:
            left = clean_char[left_i]
            right = clean_char[right_i]
            if left == right:
                left_i += 1
                right_i -= 1
                continue
            else:
                return False
        return True
