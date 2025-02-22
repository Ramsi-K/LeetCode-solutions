# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Split the traversal into nodes with their depths
        nodes = re.findall(r'(-*)(\d+)', traversal)
        
        # Initialize stack with the root node
        stack = []
        root = TreeNode(int(nodes[0][1]))
        stack.append((root, 0))  # (node, depth)
        
        for i in range(1, len(nodes)):
            dashes, val = nodes[i]
            depth = len(dashes)
            value = int(val)
            
            # Pop nodes from the stack until we find the parent
            while stack and stack[-1][1] >= depth:
                stack.pop()
            
            # Create the new node
            node = TreeNode(value)
            
            # Attach to the parent
            parent, parent_depth = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node
            
            # Push the new node onto the stack
            stack.append((node, depth))
        
        return root
      