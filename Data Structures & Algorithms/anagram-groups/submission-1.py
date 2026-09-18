class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in range(len(strs)):
            res.append(''.join(sorted(strs[i])))
        groups = {}
        for i in range(len(strs)):
            if res[i] not in groups:
                groups[res[i]] = []
            groups[res[i]].append(strs[i])

        return list(groups.values())