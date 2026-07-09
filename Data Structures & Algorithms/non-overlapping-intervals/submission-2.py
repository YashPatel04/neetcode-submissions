class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = [intervals[0]]
        count = 0
        for i in range(1,len(intervals)):
            if (res[-1][1])>(intervals[i][0]):
                count+=1
            else:
                res.append(intervals[i])
        return count