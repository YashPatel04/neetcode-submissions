class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [False]*n
        arr[-1]=True
        last = n-1
        for i in range(n-2,-1,-1):
            if(nums[i]==0): continue
            if((nums[i]+i)>=last):
                arr[i]=True
                last = i
        return arr[0]
