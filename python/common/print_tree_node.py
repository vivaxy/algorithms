def printTreeNode(treeNode, depth=0, parent=None, type=None):
    if treeNode:
        print('depth: ' + str(depth) + ', parent: ' + str(parent) +
              ', type: ' + str(type) + ', val: ' + str(treeNode.val))
        printTreeNode(treeNode.left, depth + 1, treeNode.val, 'left')
        printTreeNode(treeNode.right, depth + 1, treeNode.val, 'right')
