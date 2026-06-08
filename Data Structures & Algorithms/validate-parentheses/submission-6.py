class Solution:
    def isValid(self, s: str) -> bool:

    
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        if len(s) <= 1 or s[0] not in opening:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing and stack:
                opening_top = stack.pop()
                if (s[i] == ')' and opening_top != opening[0]) or (s[i] == '}' and opening_top != opening[1]) or (s[i] == ']' and opening_top != opening[2]):
                    return False
            elif s[i] in closing and not stack:
                return False
        if stack:
            return False
        return True

              
        