# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.value = 0
        def find_diameter(root):
            if root is None:
                return 0   
            l = find_diameter(root.left)   
            r = find_diameter(root.right)  
            self.value = max(self.value,l+r)
            return 1+max(l,r)
        find_diameter(root)  
        return self.value


        