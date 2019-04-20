import unittest

import utils


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, curr):
        if self.tail:
            self.insert_after(self.tail, curr)
        else:
            self.head = self.tail = curr
            curr.prev = curr.next = curr

    def insert_after(self, prev, curr):
        next = prev.next

        prev.next = curr
        next.prev = curr

        curr.prev = prev
        curr.next = next

        if prev is self.tail:
            self.tail = curr

    def remove(self, curr):
        prev = curr.prev
        next = curr.next

        prev.next = next
        next.prev = prev

        curr.prev = None
        curr.next = None

        if curr is self.head:
            if curr is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = next
        elif curr is self.tail:
            self.tail = prev

    def popleft(self):
        head = self.head
        self.remove(head)
        return head


# O(capacity) space. Hash table, linked list.
class LRUCache:
    # O(1) time. O(1) space.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_list = LinkedList()
        self.node_dict = {}

    # O(1) time. O(1) space.
    def get(self, key: int) -> int:
        curr = self._get_node(key)
        return curr.val if curr else -1

    # O(1) time. O(1) space.
    def put(self, key: int, value: int) -> None:
        curr = self._get_node(key)

        if curr:
            curr.val = value
        else:
            curr = ListNode(key, value)
            self.node_list.append(curr)
            self.node_dict[key] = curr

            if len(self.node_dict) > self.capacity:
                head = self.node_list.popleft()
                del self.node_dict[head.key]

    # O(1) time. O(1) space.
    def _get_node(self, key):
        curr = self.node_dict.get(key)
        if not curr:
            return None

        if curr is not self.node_list.tail:
            self.node_list.remove(curr)
            self.node_list.append(curr)

        return curr


class Test(unittest.TestCase):
    def test(self):
        cls = LRUCache
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
