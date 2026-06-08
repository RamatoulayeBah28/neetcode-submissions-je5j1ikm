class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {')':'(', ']':'[','}':'{'}
        for p in s:
            if p in closeToOpen:
                if not stack:
                    return False
                match = stack.pop()
                if closeToOpen[p] != match:
                    return False
                
            elif p in closeToOpen.values():
                stack.append(p)
        if stack:
            return False
        return True

              
        