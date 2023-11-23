class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = set()
        left = 0
        right = 0
        maxlength = 0

        for right in range(n):
            if s[right] not in res:
                res.add(s[right])
                maxlength = max(maxlength , right - left +1)
            else:
                while(s[right] in res):
                    res.remove(s[left])
                    left+=1
                res.add(s[right])

        return  maxlength


