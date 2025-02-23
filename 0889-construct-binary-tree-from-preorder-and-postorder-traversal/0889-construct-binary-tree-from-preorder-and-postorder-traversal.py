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
        
        # Create the root node
        root = TreeNode(preorder[0])
        stack = [root]
        post_index = 0  # Pointer for postorder traversal
        
        # Iterate through the preorder traversal
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            
            # If the top of the stack is not the current postorder element,
            # the new node is the left child of the top of the stack
            if stack[-1].val != postorder[post_index]:
                stack[-1].left = node
            else:
                # Pop from the stack until the top no longer matches the postorder traversal
                while stack and stack[-1].val == postorder[post_index]:
                    stack.pop()
                    post_index += 1
                # The new node is the right child of the last popped node
                stack[-1].right = node
            
            # Push the new node onto the stack
            stack.append(node)
        
        return root

            