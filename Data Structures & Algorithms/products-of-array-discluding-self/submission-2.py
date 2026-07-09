class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currProd=1
        arr=[1 for i in nums]
        zeroes=[]
        for i in range(len(nums)):
            if(nums[i]==0):
                zeroes.append(i)
            arr[i]*=currProd
            currProd*=nums[i] if nums[i]!=0 else 1
        currProd=1
        if(len(zeroes)>1):
            return [0 for i in nums]
        for i in range(len(nums)-1,-1,-1):
            arr[i]*=currProd
            currProd*=nums[i] if nums[i]!=0 else 1
        if(len(zeroes)==1):
            index = zeroes.pop()
            for i in range(len(nums)):
                if i==index:
                    continue
                arr[i]=0
        return arr