class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the length of the lists are not equal 
        if len(s) != len(t):
            # we can return False
            return False
        # # return sorted(s) == sorted(t)
        # return sorted(s) == sorted(t)
        dict_s, dict_t = {}, {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        return dict_t == dict_s
        
        
         
        