class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 0
        for _ in range(n):
            temp=prev
            prev=curr
            curr+=temp
        return curr