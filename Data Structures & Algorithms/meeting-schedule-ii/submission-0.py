"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # Date Solved: 14 July 2026, Tuesday
    # Blind 75
    # Refer: codestorywithMIK. NeetCode's video approach uses 2 pointers but is similar to this.
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Using Line Sweep
        # Time : O(n log n)
        # Space : O(n) to store events in dict

        events = defaultdict(int)

        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1

        result = 0
        count = 0

        for time in sorted(events):
            count += events[time]
            result = max(result, count)

        return result
