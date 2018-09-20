def treeNodeToList(treeNode):
    ans = []
    remainingTreeNodes = [treeNode]
    while len(remainingTreeNodes) and not all(map(lambda x: x == None, remainingTreeNodes)):
        cur = remainingTreeNodes.pop(0)
        if cur == None:
            ans.append(None)
        else:
            ans.append(cur.val)
            if cur.left:
                remainingTreeNodes.append(cur.left)
            else:
                remainingTreeNodes.append(None)
            if cur.right:
                remainingTreeNodes.append(cur.right)
            else:
                remainingTreeNodes.append(None)
    return ans
