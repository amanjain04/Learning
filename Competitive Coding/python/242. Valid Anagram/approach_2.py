class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        a = {}
        for i in s:
            a[i] = a.get(i,0)+1
        for j in t:
            if j in a:
                a[j] -= 1
            else:
                return False

        for k,v in a.items():
            if (v!=0):
                return False

        return True
