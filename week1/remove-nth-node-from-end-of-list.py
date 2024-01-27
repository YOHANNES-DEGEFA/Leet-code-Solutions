# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        length = 0
        while head:
            length+=1
            head = head.next
            
        print(length)
        x = length-n
        counter = 0
        while prev:
            if counter == x:
                prev.next = prev.next.next
            prev = prev.next
            counter +=1
            
            
            
        return dummy.next
                