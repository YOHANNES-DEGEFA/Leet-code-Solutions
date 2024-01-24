# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = head 
        while head:
            
            while head.next and head.next.val == head.val: 
                head.next = head.next.next
            head = head.next
        return answer 