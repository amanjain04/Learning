class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in numset:
            if i-1 not in numset:
                length = 0 
                while (i+length) in numset:
                    length+=1
                longest = max(length,longest)

        return longest
                


        