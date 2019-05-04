from typing import List
from .tree_node import TreeNode


def listToTreeNode(l: List) -> TreeNode:
    root = None
    parents = []
    isLeft = True
    def popNone() -> None:
        while len(parents) and parents[0] == None:
            parents.pop(0)
    for i in l:
        if root == None:
            if i == None:
                return root
            root = TreeNode(i)
            parents.append(root)
            continue
        if isLeft:
            if i == None:
                popNone()
                isLeft = False
                parents.append(None)
                continue
            node = TreeNode(i)
            popNone()
            parents[0].left = node
            parents.append(node)
            isLeft = False
            continue
        if i == None:
            isLeft = True
            parents.pop(0)
            popNone()
            parents.append(None)
            continue
        node = TreeNode(i)
        popNone()
        parent = parents.pop(0)
        parent.right = node
        parents.append(node)
        isLeft = True
    return root
