class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the length of the lists are not equal 
        if len(s) != len(t):
            # we can return False
            return False
        # return sorted(s) == sorted(t)
        return sorted(s) == sorted(t)

         
        