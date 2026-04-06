class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Understand: we want to return the k most frequent elements from the integer list
        # Match: Frequency map sorted by value
        # initialize a dict
        freq_dict = {}
        # initialize a result list
        result = []
        # for num in nums:
        for num in nums:
            # increment count of num in the dict
            freq_dict[num] = freq_dict.get(num, 0) + 1
        # for i, v in enumerate dict.items
        new_sorted = dict(sorted(freq_dict.items(), key=lambda item:item[1], reverse=True))

        for key, count in new_sorted.items():
            # new_sorted = sorted dict
            # while k > 0:
            if k > 0:
                # result.append(i)
                result.append(key)
                # k -= 1
                k-=1
        return result
            
        