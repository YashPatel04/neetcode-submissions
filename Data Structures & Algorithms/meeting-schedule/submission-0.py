"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0: return True
        # NON OVERLAPPING INTERVALS
        # 1.) sort by start time
        intervals.sort(key=lambda x:x.start)
        # 2.) check for overlaps
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if (res[-1].end)>(intervals[i].start):
                return False
            res.append(intervals[i])
        return True
