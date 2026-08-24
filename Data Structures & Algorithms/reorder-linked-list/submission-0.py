# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[j].next = nodes[i].next
            nodes[i].next = nodes[j]

            i += 1
            j -= 1

        nodes[i].next = None
        return 