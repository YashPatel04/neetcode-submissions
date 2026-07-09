from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(list)
        for i, j in enumerate(nums):
            if (target-j) in values.keys():
                return [min(i, values[target-j][0]), max(i, values[target-j][0])]
            values[j].append(i)
        return []