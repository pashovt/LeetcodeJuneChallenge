# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return None
        
        #print(root)
        root.left, root.right = root.right, root.left
        
        #print(root)
        
        #print('------------------')
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

Solution.invertTree([4,2,7,1,3,6,9])
