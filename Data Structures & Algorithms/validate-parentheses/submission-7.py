class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closingBrackets = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in closingBrackets:
                if stack and stack[-1] == closingBrackets[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False