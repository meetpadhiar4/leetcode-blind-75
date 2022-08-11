# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        before_start, end = dummy, head
        i = 0
        while end:
            i += 1
            if i % k == 0:
                start = before_start.next
                after_end = end.next
                self.reverse(start, end)
                before_start.next = end
                start.next = after_end
                before_start = start
                end = after_end
            else:
                end = end.next
        
        return dummy.next
        
    def reverse(self, start, end):
        prev, curr, next = None, start, start.next
        while prev != end:
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = next.next
        
