from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(list)
        for j, i in enumerate(nums):
            if len(values[target-i])!=0:
                return [min(j, values[target-i][0]), max(j, values[target-i][0])]
            values[i].append(j)
        return []