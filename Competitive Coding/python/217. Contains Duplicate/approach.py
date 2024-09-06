class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = dict()

        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]]  = i
            else:
                if ((i - res[nums[i]])  <=k):
                    return True
                res[nums[i]] = i

        return False
