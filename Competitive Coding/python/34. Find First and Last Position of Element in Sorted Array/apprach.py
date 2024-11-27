class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums)==0):
            return [-1,-1]
        l = 0
        r = len(nums)-1

        while(l<=r and l<len(nums) and r>=0):
            mid = (l+r)//2
            if (nums[mid]>target):
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                if nums[l] == target and nums[r] == target:
                    return[l,r]

                if nums[l]!= target:
                    l+=1

                if nums[r]!= target:
                    r-=1

        return [-1,-1]
        