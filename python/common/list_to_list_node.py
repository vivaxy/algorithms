from .list_node import ListNode


def listToListNode(arr):
    head = None
    cur = head
    for item in arr:
        if head == None:
            head = ListNode(item)
            cur = head
        else:
            node = ListNode(item)
            cur.next = node
            cur = node
    return head
