def listNodeToList(head):
    ans = []
    cur = head
    while cur:
        ans.append(cur.val)
        cur = cur.next
    return ans
