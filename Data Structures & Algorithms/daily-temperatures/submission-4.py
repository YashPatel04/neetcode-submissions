class Solution:
    def dailyTemperatures(self, tempratures: List[int]) -> List[int]:
        indexes=[] # LIFO
        arr=[0 for _ in tempratures]
        for i in range(len(tempratures)-1, -1, -1):
            if(indexes and tempratures[indexes[-1]]<=tempratures[i]):
                # pop until a warmer tempratures appear
                while(indexes and tempratures[indexes[-1]]<=tempratures[i]):
                    indexes.pop()
                arr[i]=indexes[-1]-i if indexes else 0
            else:
                arr[i]=indexes[-1]-i if indexes else 0
            indexes.append(i)
        return arr