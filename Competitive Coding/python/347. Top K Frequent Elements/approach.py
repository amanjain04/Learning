class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        freq = [[] for i in range(len(nums)+1)]

        res = []

        for i in nums:
            my_dict[i] = 1+my_dict.get(i,0)

        for i,j in my_dict.items():
            freq[j].append(i)

        for i in range(len(freq)-1 , 0 , -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res