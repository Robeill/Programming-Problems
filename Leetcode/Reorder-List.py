# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid , prev = slow , None
        while mid:
            next_mid = mid.next
            mid.next = prev
            prev = mid
            mid = next_mid
        first , last = head , prev
        while last.next:
            first.next , first = last , first.next
            last.next , last = first , last.next
        return head

        