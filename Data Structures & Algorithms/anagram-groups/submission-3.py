class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for word in strs:
            vals = list(word)
            vals.sort()
            hashmap["".join(vals)].append(word)
        return list(hashmap.values())