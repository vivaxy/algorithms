from .tree_node import TreeNode


def listToTreeNode(l):
    root = None
    parents = []
    left = True
    for i in l:
        if root == None:
            if i == None:
                return root
            root = TreeNode(i)
            parents.append(root)
            continue
        if left:
            if i == None:
                left = False
                parents.append(None)
                continue
            node = TreeNode(i)
            parents[0].left = node
            parents.append(node)
            left = False
            continue
        if i == None:
            left = True
            parents.pop(0)
            parents.append(None)
            continue
        node = TreeNode(i)
        parents.pop(0).right = node
        parents.append(node)
        left = True
    return root
