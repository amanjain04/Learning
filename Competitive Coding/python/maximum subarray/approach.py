class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = float('-inf')
        temp =0
        for i in nums:
            temp +=i
            if (temp > res):
                res = temp
            if temp <0:
                temp=0



        return res
