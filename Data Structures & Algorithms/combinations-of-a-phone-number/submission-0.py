class Solution:
    def letterCombinations(self, nums: str) -> List[str]:
        if nums=="": return []
        digits = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res = []
        def dfs(s, i):
            if i>=len(nums):
                res.append(s)
                return
            arr = digits[nums[i]]
            for w in arr:
                dfs(s+w, i+1)
        dfs("", 0)
        return res