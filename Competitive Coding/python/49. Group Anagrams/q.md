class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sorted_string = ''.join(sorted(i))
            if sorted_string not in res:
                res[sorted_string]=[i]
            else:
                res[sorted_string].append(i)

        result = []
        for i in res.values():
            result.append(i)
        return result