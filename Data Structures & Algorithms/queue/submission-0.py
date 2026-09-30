class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        curr = ListNode(value)
        last = self.tail.prev
        self.tail.prev = curr
        curr.next = self.tail
        last.next = curr
        curr.prev = last

    def appendleft(self, value: int) -> None:
        curr = ListNode(value)
        next = self.head.next
        self.head.next = curr
        curr.prev = self.head
        curr.next = next
        next.prev = curr

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.tail.prev
        before = target.prev
        value = target.val
        before.next = self.tail
        self.tail.prev = before
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target = self.head.next
        value = target.val
        after = target.next
        self.head.next = after
        after.prev = self.head
        return value



