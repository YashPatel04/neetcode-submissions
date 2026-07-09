"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0: return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s,e=0,0
        rooms = 0
        max_rooms = 1
        while s<len(starts) and e<len(ends):
            if starts[s]<ends[e]:
                s+=1
                rooms+=1
            else:
                e+=1
                rooms-=1
            max_rooms = max(rooms, max_rooms)
        return max_rooms