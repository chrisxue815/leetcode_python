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

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1

        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        inserted = ListNode(val)
        inserted.next = self.head
        self.head = inserted

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        inserted = ListNode(val)

        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = inserted
        else:
            self.head = inserted

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
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

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
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
        cls = MyLinkedList
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
