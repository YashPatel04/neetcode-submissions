class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            key=i
            key = "".join(sorted(key))
            arr = hashmap.get(key, [])
            arr.append(i)
            hashmap[key]=arr
        return [l for l in hashmap.values()]