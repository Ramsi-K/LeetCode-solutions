class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = [x for x in path.split("/") if x]

        for name in path:
            if stack and name=="..":
                stack.pop()
            elif name in [".", ".."]:
                continue
            else:
                stack.append(name)

        return "/" + "/".join(stack)
        