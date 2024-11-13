class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sys.maxsize
        nums.sort()

        for i, j in enumerate(nums):
            l = i+1
            r = len(nums)-1

            while (l<r):
                temp = j + nums[l] + nums[r]
                if (temp > target):
                    r -= 1
                elif (temp < target):
                    l += 1
                else:
                    return temp
                if (abs(res-target)>abs(temp-target)):
                    res = temp
                

        return res
                    