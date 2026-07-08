/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int depth(TreeNode root,int value){
        if(root == null){
            return value;
        }
        return Math.max(depth(root.left,value+1),depth(root.right,value+1));
    }
    public int maxDepth(TreeNode root) {
        return depth(root,0);
    }
}
