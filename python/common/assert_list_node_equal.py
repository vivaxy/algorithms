def assertListNodeEqual(list1, list2):
    if not list1 and not list2:
        return True
    if list1 and list2:
        if (list1.val != list2.val):
            print(list1.val + ' != ' + list2.val)
            return False
        return assertListNodeEqual(list1.next, list2.next)
    print(list1 + ' != ' + list2)
    return False
