class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize empty res
        res = ""
        # for each string in the list
        for s in strs:
            res+= str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # initialize an empty list and a pointer
        res, i = [], 0
        # while i is less than length of s:
        while i < len(s):
            j = i
            # move pointer j forward till we find #
            while s[j] != "#":
                j+=1
            # store the length we found
            length = int(s[i:j])
            # append the extracted string to res list
            res.append(s[j+1:j+1+length])
            # move i forward by length to continue decoding
            i = j + 1 + length
        return res
