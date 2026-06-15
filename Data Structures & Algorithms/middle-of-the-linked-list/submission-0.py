# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 15 June 2026, Monday, inspired by LeetCode POTD
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:  # fast.next.next can be the last node or None (node after the last node)
            fast = fast.next.next
            slow = slow.next
        return slow
