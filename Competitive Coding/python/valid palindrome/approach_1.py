class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False

        temp = x
        res =0
        while (x!=0):
            s = x%10
            res = s + res*10
            x = x//10

        if res == temp:
            return True

        else:
            return False
