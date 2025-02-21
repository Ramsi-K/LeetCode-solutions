# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        if root:
            # Recover the tree: assign the root value as 0.
            root.val = 0
            queue = deque([root])
            self.values.add(0)
            
            # Use BFS to traverse and recover the tree.
            while queue:
                node = queue.popleft()
                if node.left:
                    node.left.val = 2 * node.val + 1
                    self.values.add(node.left.val)
                    queue.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    self.values.add(node.right.val)
                    queue.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)