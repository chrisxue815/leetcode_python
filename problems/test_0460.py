import unittest

import utils


class ListNode:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        self.count = 1

    def add_before(self, curr):
        prev = self.prev
        prev.next = curr
        curr.prev = prev
        curr.next = self
        self.prev = curr

    def add_after(self, curr):
        nxt = self.next
        self.next = curr
        curr.prev = self
        curr.next = nxt
        nxt.prev = curr

    def remove(self):
        prev = self.prev
        nxt = self.next
        prev.next = nxt
        nxt.prev = prev


class LinkedList:
    def __init__(self):
        self.sentinel = ListNode(None, None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def add_head(self, curr):
        self.sentinel.add_after(curr)

    def head(self):
        return self.sentinel.next


# O(capacity) space. Hash table, linked list.
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = LinkedList()
        self.keys = {}
        self.counts = {}

    def get(self, key: int) -> int:
        curr = self.keys.get(key)
        if not curr:
            return -1

        self._increment(curr)

        return curr.val

    def put(self, key: int, value: int) -> None:
        curr = self.keys.get(key)
        if curr:
            curr.val = value
            self._increment(curr)
        elif self.capacity:
            if len(self.keys) >= self.capacity:
                self._remove_head()

            curr = ListNode(key, value)
            self.keys[key] = curr
            self._add(curr)

    def _increment(self, curr):
        curr_tail = self.counts[curr.count]
        next_tail = self.counts.get(curr.count + 1)

        self._remove_from_counts(curr)

        if next_tail or curr is not curr_tail:
            curr.remove()
            (next_tail or curr_tail).add_after(curr)

        curr.count += 1
        self.counts[curr.count] = curr

    def _remove_from_counts(self, curr):
        tail = self.counts[curr.count]
        if curr is not tail:
            return

        prev = tail.prev
        if prev and prev.count == tail.count:
            self.counts[curr.count] = prev
        else:
            del self.counts[curr.count]

    def _remove_head(self):
        curr = self.queue.head()
        del self.keys[curr.key]
        self._remove_from_counts(curr)
        curr.remove()

    def _add(self, curr):
        tail = self.counts.get(curr.count)
        if tail:
            tail.add_after(curr)
        else:
            self.queue.add_head(curr)

        self.counts[curr.count] = curr


class Test(unittest.TestCase):
    def test(self):
        cls = LFUCache
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
