import unittest

import utils


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.head:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        inserted = ListNode(val)
        inserted.next = self.head
        self.head = inserted

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        inserted = ListNode(val)

        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = inserted
        else:
            self.head = inserted

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
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
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
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
