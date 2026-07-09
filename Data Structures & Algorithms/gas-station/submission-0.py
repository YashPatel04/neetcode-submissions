class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        currGas = 0
        newCost = cost+cost
        newGas = gas+gas
        cost = newCost
        gas = newGas
        for i in range(0, (len(cost)//2)):
            currGas+=gas[i]
            if cost[i]>currGas:
                start = i+1
                currGas = 0
            else:
                currGas -= cost[i]
        for i in range(len(cost)//2, len(cost)):
            currGas+=gas[i]
            if cost[i]>currGas:
                return -1
            else:
                currGas -= cost[i]
        return start