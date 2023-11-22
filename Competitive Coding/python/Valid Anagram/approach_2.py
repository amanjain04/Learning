class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        a = dict()
        for i in s:
            a[i] = a.get(i,0)+1
        for j in t:
            if j in a:
                a[j] = a.get(j,0)-1
            else:
                False

        for k,v in a.items():
            if (v!=0):
                return False

        return True
