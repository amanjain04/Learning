class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num

        heapify(nums)
        res = 0
        while(k):
            res = heappop(nums)
            k-=1
        
        return -res
        