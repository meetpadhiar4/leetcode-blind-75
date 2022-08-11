# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap, dummy, counter = [], ListNode(), 0
        curr = dummy
        for i in lists:
            if i:
                heapq.heappush(min_heap, (i.val, counter, i))
                counter += 1
        
        while min_heap:
            node = heapq.heappop(min_heap)[2]
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next
