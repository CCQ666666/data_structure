class linkList:
    def __init__(self, val):
        self.val = val
        self.next = None


# 迭代反转
def reverse_linklist1(head):
    if not head or not head.next:
        return head
    pre = head
    cur = head.next
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    head.next = None
    return pre


# 递归反转
def reverse_linklist2(head):
    if not head.next:
        return head
    last = reverse_linklist2(head.next)
    head.next.next = head
    head.next = None
    return last


# 递归反转前N个节点
def reverse_n_linklist(head, n):
    successor = None

    def reverse(head, n):
        nonlocal successor
        if n == 1:
            successor = head.next
            return head
        last = reverse(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return last

    last = reverse(head, n)
    return last


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = linkList(nums[0])
    node = head
    for num in nums[1:]:
        node.next = linkList(num)
        node = node.next
    # reversed = reverse_linklist1(head)
    # reversed = reverse_linklist2(head)
    reversed = reverse_n_linklist(head, 2)
    print()
