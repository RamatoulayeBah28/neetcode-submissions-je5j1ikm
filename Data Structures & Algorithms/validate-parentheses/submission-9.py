class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(',']':'[','}':'{'}
        for bracket in s:
            
            if stack and bracket in matching:
                if matching.get(bracket) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
        