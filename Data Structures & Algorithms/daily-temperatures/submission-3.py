class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idxStack=[]
        arr=[0 for i in range(len(temperatures))]
        for i in range(len(temperatures)-1, -1, -1):
            if idxStack and temperatures[idxStack[-1]]<=temperatures[i]:
                while(idxStack):
                    if temperatures[idxStack[-1]]<=temperatures[i]:
                        idxStack.pop()
                    else:
                        break
                arr[i]=idxStack[-1]-i if idxStack else 0
                idxStack.append(i)
            else:
                if not idxStack:
                    arr[i]=0
                    idxStack.append(i)
                else:
                    arr[i]= idxStack[-1]-i
                    idxStack.append(i)
        return arr