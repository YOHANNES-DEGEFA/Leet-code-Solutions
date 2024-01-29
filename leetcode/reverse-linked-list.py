# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        currentNode = head
        while currentNode:
            #store the reference of the next Node  using the variable nextNode
            nextNode     = currentNode.next
            # manipulate the current node's next pointer field to point to the previousNode
            currentNode.next = previousNode
            #update previousNode to current 
            previousNode = currentNode
            # move current node one node forward
            currentNode = nextNode
        head = previousNode

        return head

        

        