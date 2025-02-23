# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        # Find the index of the left subtree root in postorder
        left_root_val = preorder[1]
        left_root_idx = postorder.index(left_root_val)
        
        # Determine the size of the left subtree
        left_size = left_root_idx + 1
        
        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:1+left_size], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[1+left_size:], postorder[left_size:-1])
        
        return root

            