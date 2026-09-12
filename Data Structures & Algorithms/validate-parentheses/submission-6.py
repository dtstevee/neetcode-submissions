class Solution:
    def isValid(self, s: str) -> bool:
        pair_hash = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        char_stack = [None]
        for char in s:
            if char in pair_hash:
                val = char_stack[-1]

                if val != pair_hash[char]:
                    return False
                
                char_stack.pop()

            else:
                char_stack.append(char)
        return len(char_stack) == 1
