class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = defaultdict(list)
        for index, value in enumerate(nums):
            if target-value in vals:
                return[min(vals[target-value][0], index), max(vals[target-value][0], index)]
            vals[value].append(index)
        return [0,0]