class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0