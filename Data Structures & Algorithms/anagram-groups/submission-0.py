class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalLst = []
        sortedMap = {}
        for word in strs:
            sortedWrd = "".join(sorted(word))
            if sortedWrd not in sortedMap:
                sortedMap[sortedWrd] = []
            sortedMap[sortedWrd].append(word)
        return list(sortedMap.values())
            
        

        