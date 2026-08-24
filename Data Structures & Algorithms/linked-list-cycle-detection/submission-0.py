# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        seen.add(head)
        curr = head
        while curr and curr.next:
            if curr.next in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False