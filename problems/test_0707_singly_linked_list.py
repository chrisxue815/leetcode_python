import unittest

import utils


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        inserted = ListNode(val)
        inserted.next = self.head
        self.head = inserted

    def addAtTail(self, val: int) -> None:
        inserted = ListNode(val)

        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = inserted
        else:
            self.head = inserted

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        if not self.head:
            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next
            if not curr:
                return

        inserted = ListNode(val)
        inserted.next = curr.next
        curr.next = inserted

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next
            if not curr:
                return

        if curr.next:
            curr.next = curr.next.next


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MyLinkedList)


if __name__ == '__main__':
    unittest.main()
