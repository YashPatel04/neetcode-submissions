class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first binary sort by 0th element
        intervals.sort(key=lambda x: x[0])
        # then merge ovelapping intervals
        res = [intervals[0]]
        i=1
        while(i<len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1]=[min(res[-1][0],intervals[i][0]), max(res[-1][1],intervals[i][1])]
            else:
                res.append(intervals[i])
            i+=1
        return res