# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.get_length(head)
        pos = length - n + 1
        if pos == 1:
            return head.next
        curr_len, curr = 1, head
        while curr_len != pos - 1:
            curr_len += 1
            curr = curr.next
        curr.next = curr.next.next
        
        return head
               
    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        
        return count
