class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            hashmap[key].append(i)
        return [value for value in hashmap.values()]