# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def travel(node, k):
            if (node is None):
                return
            
            if (node.left is not None):
                travel(node.left, k)
            
            if (len(lst) == k):
                return
            lst.append(node.val)
            
            if (node.right is not None):
                travel(node.right, k)
        
        travel(root, k)
        
        return lst[-1]