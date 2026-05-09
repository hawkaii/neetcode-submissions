/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
           if (!root) return true;

    let left_height = maxHeight(root.left);
    let right_height = maxHeight(root.right);
    if (Math.abs(left_height - right_height) > 1) {
      return false;
    }

    return this.isBalanced(root.left) && this.isBalanced(root.right);

    function maxHeight(root) {
      if (!root) return true;
      return 1 + Math.max(maxHeight(root.left), maxHeight(root.right));
    }


    }
}
