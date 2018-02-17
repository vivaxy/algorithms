def assertListNodeEqual(list1, list2):
    if not list1 and not list2:
        return True
    if list1 and list2:
        return list1.val == list2.val and assertListNodeEqual(list1.next, list2.next)
    return False
