# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Initialize stacks for left (smallest to largest) and right (largest to smallest) pointers
        left_stack = []
        node = root
        while node:
            left_stack.append(node)
            node = node.left
        
        right_stack = []
        node = root
        while node:
            right_stack.append(node)
            node = node.right
        
        # Function to get next smallest element
        def get_left():
            if not left_stack:
                return None
            node = left_stack.pop()
            current = node.right
            while current:
                left_stack.append(current)
                current = current.left
            return node.val
        
        # Function to get next largest element
        def get_right():
            if not right_stack:
                return None
            node = right_stack.pop()
            current = node.left
            while current:
                right_stack.append(current)
                current = current.right
            return node.val
        
        # Initialize left and right values
        left_val = get_left()
        right_val = get_right()
        
        while left_val is not None and right_val is not None and left_val < right_val:
            current_sum = left_val + right_val
            if current_sum == k:
                return True
            elif current_sum < k:
                left_val = get_left()
            else:
                right_val = get_right()
        
        return False