class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if (s[i] not in t) or (t[j] not in s):
        #             return False
        # return True
        if sorted(s) == sorted(t):
            return True
        return False