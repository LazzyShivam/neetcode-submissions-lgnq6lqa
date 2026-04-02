# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count_dept(root,count):
            if root == None:
                return count
            return 1+max(count_dept(root.left,count),count_dept(root.right,count))    
        return count_dept(root,0)