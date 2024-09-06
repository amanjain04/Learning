Time Complexity : O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff not in result:
                result[nums[i]]=i

            else:
                return [result[diff],i]
