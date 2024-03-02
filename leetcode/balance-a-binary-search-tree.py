# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        def inOrder(root): 
            if not root: 
                return 

            inOrder(root.left)
            nums.append(root.val)
            inOrder(root.right)

        inOrder(root)


        def buildBST(nums): 

            if not nums: 
                return 
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = buildBST(nums[:mid])
            root.right = buildBST(nums[mid+1:])

            return root 


        return buildBST(nums)

        