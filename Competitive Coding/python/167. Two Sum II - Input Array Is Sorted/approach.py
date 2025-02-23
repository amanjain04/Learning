class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in my_dict:
                return [my_dict[diff]+1,i+1]
            else:
                my_dict[numbers[i]] = i
            
        