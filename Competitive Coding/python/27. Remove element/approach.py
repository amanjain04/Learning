class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while (i<len(nums) and i>=j):
            if (nums[i] != val):
                nums[j] = nums[i]
                j+=1
                i+=1
            else:
                i+=1
            
        return j


        