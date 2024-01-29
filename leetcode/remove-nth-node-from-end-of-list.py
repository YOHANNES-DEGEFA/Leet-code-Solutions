# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        answer = head 
        list_len = 0 
        while temp: 
            list_len += 1
            temp = temp.next

        target_pos = list_len -n #len = 5   - n = 2   gives 3

        if target_pos == 0: # if we are required to remove the first element 
            answer = answer.next 
        else: 
            while target_pos > 1: 
                head = head.next 
                target_pos -= 1 
            head.next = head.next.next
        
        return answer
        