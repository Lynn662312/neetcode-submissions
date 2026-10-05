class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if the key (after sort) doesnt exist, create a new default empty list
        res = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)
        return list(res.values())