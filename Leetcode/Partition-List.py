# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list_s = ListNode(0)
        list_g = ListNode(0)
        small = list_s
        big = list_g

        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        
        small.next = list_g.next
        big.next = None

        return list_s.next

