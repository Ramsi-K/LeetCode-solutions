from collections import defaultdict
from typing import List

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

def build_tree(paths: List[List[str]]) -> Node:
    root = Node("")
    for path in paths:
        curr = root
        for folder in path:
            if folder not in curr.children:
                curr.children[folder] = Node(folder)
            curr = curr.children[folder]
    return root

def collect_signatures(node: Node, sig_map: dict) -> str:
    if not node.children:
        return ""

    sig_parts = []
    for name in sorted(node.children.keys()):
        child_sig = collect_signatures(node.children[name], sig_map)
        sig_parts.append(f"{name}({child_sig})")

    sig = "".join(sig_parts)
    sig_map[sig] += 1
    return sig

def filter_tree(node: Node, sig_map: dict, current_path: List[str], result: List[List[str]]) -> None:
    # Get the signature of this node
    if node.children:
        sig_parts = []
        for name in sorted(node.children.keys()):
            child_sig = get_signature(node.children[name], sig_map)
            sig_parts.append(f"{name}({child_sig})")
        node_sig = "".join(sig_parts)
        if sig_map[node_sig] >= 2:
            return  # duplicate subtree → skip this entire branch

    if node.name:  # skip root's empty name
        result.append(current_path + [node.name])

    for name in sorted(node.children.keys()):
        filter_tree(node.children[name], sig_map, current_path + [node.name], result)

def get_signature(node: Node, sig_map: dict) -> str:
    # Reconstruct the signature to match what was done in collect_signatures
    if not node.children:
        return ""
    sig_parts = []
    for name in sorted(node.children.keys()):
        sig_parts.append(f"{name}({get_signature(node.children[name], sig_map)})")
    return "".join(sig_parts)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = build_tree(paths)
        sig_map = defaultdict(int)
        collect_signatures(root, sig_map)

        result = []
        for name in sorted(root.children.keys()):
            filter_tree(root.children[name], sig_map, [], result)
        return result

