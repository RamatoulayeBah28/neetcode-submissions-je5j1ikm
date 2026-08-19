class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        arr = []
        for n, f in freq.items():
            arr.append([f, n])
        arr.sort()
        res = []
        while len(res) < k:
            print(res)
            res.append(arr.pop()[1])
        return res

        