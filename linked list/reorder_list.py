def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    curr = head
    for i in range(len(stack)//2):
        node = stack.pop()
        next = curr.next
        curr.next = node
        node.next = next
        curr = next
    curr.next=None   