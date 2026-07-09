class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 0
        for _ in range(n, 0,-1):
            temp = one
            one+=two
            two = temp
        return one