"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # Blind 75
    # Refer: NC Ashish, solved on my own after practicing other "Intervals" problem.
    # No codestorywithMIK and NeetCode's approach similar to mine.
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time: O(nlogn), Space: O(1) ignoring extra space used by sorting
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < prev_end:
                return False
            prev_end = end
        return True
