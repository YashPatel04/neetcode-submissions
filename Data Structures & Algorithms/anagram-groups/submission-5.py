class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for word in strs:
            alpha=[0 for _ in range(26)]
            for i in word:
                alpha[ord(i)-ord("a")]+=1
            map[tuple(alpha)].append(word)
        return list(map.values())