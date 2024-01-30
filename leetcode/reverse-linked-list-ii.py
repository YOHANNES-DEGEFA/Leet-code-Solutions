# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr =  []
        ans = dummy = ListNode()
        while head:
            arr.append(head.val)
            head = head.next
        arr[left-1:right] = reversed(arr[left-1:right])
      
        for i in range(len(arr)):
            dummy.next = ListNode(arr[i])
            dummy  = dummy.next
        return ans.next


        






