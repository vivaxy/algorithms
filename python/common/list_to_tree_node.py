from typing import List
from .tree_node import TreeNode


def listToTreeNode(l: List) -> TreeNode:
    root = None
    parents = []
    isLeft = True
    for i in l:
        if root == None:
            if i == None:
                return root
            root = TreeNode(i)
            parents.append(root)
            continue
        if isLeft:
            if i == None:
                while len(parents) and parents[0] == None:
                    parents.pop(0)
                isLeft = False
                parents.append(None)
                continue
            node = TreeNode(i)
            parents[0].left = node
            parents.append(node)
            isLeft = False
            continue
        if i == None:
            isLeft = True
            parents.pop(0)
            while not parents[0]:
                parents.pop(0)
            parents.append(None)
            continue
        node = TreeNode(i)
        parent = parents.pop(0)
        while not parent:
            parent = parents.pop(0)
        parent.right = node
        parents.append(node)
        isLeft = True
    return root
