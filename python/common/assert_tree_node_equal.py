def assertTreeNodeEqual(tree1, tree2):
    if tree1.val != tree2.val:
        print(str(tree1.val) + ' != ' + str(tree2.val))
        return False
    if tree1.left == None and tree2.left == None:
        if tree1.right == None and tree2.right == None:
            return True
        return assertTreeNodeEqual(tree1.right, tree2.right)
    if tree1.right == None and tree2.right == None:
        return assertTreeNodeEqual(tree1.left, tree2.left)
    return assertTreeNodeEqual(tree1.left, tree2.left) and assertTreeNodeEqual(tree1.right, tree2.right)
