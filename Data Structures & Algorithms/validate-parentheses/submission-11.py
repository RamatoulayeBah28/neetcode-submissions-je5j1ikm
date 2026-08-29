class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        match = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if not stack and c in match.keys():
                return False
            elif stack and c in match.keys():
                print(c)
                print("Closing bracket check:", stack)
                if stack[-1] != match[c]:
                    print(stack[-1])
                    return False
                stack.pop()
            
            if c in match.values():
                stack.append(c)
        print("Last state of stack", stack)
        return True if not stack else False
        