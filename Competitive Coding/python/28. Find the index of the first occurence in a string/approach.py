class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while (i<len(haystack)):
            if (haystack[i] == needle[0]):
                j = 0
                while(j<len(needle) and i<len(haystack) and haystack[i]==needle[j]):
                    i+=1
                    j+=1
                    if (j==len(needle)):
                        return i-j
            else:
                i+=1
        return -1
        