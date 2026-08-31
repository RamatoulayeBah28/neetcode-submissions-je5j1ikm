class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize frequency list
        freq = {}

        # count freq of each num
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
 
        # initialize empty array and append freq and number
        arr = []
        for n, f in freq.items():
            arr.append([f, n])
        # sort the array
        arr.sort()
        res = []
        # while the length of the result array is less than k, append the top number from arr
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
     
        