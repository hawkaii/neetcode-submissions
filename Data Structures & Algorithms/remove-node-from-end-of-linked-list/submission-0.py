# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0 
        map = {}
        cur = head
        while cur:
            map[count] = cur
            count+=1
            cur = cur.next
        
        t = count - n  
        if t == 0:
            return head.next
        if map[t-1]:
            map[t-1].next = map[t].next
        return head
        



