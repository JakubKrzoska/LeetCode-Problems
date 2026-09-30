class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        curr = ListNode(val)
        if self.head.next == None:
            self.tail = curr
        curr.next = self.head.next
        self.head.next = curr

    def insertTail(self, val: int) -> None:
        curr = ListNode(val)
        self.tail.next = curr
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr and i < index:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
