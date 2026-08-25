# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        
        if n == len(arr):
            return head.next

        arr[len(arr)-n-1].next = arr[len(arr)-n].next
        arr[len(arr)-1].next = None

        return head
        