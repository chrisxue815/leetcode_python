import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_array(vals):
        if not vals:
            return None
        root_parent = ListNode(0)
        parent = root_parent

        for val in vals:
            curr = ListNode(val)
            parent.next = curr
            parent = curr

        return root_parent.next

    @staticmethod
    def to_array(root):
        vals = []
        while root:
            vals.append(root.val)
            root = root.next
        return vals

    @staticmethod
    def reverse_list(root):
        prev = None
        while root:
            next_ = root.next
            root.next = prev
            prev = root
            root = next_
        return prev

    @staticmethod
    def count(root):
        result = 0
        while root:
            result += 1
            root = root.next
        return result

    @staticmethod
    def mid_right(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def mid_left(head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Test(unittest.TestCase):
    def test_reverse_list(self):
        self._test_reverse_list([1, 2, 3], [3, 2, 1])
        self._test_reverse_list([1, 2], [2, 1])
        self._test_reverse_list([1], [1])
        self._test_reverse_list([], [])

    def _test_reverse_list(self, head, expected):
        head = ListNode.from_array(head)
        actual = ListNode.reverse_list(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)

    def test_count(self):
        self._test_count([1, 2], 2)
        self._test_count([1], 1)
        self._test_count([], 0)

    def _test_count(self, head, expected):
        head = ListNode.from_array(head)
        actual = ListNode.count(head)
        self.assertEqual(expected, actual)

    def test_mid_right(self):
        self._test_mid_right([1, 2, 3], 2)
        self._test_mid_right([1, 2], 2)
        self._test_mid_right([], None)

    def _test_mid_right(self, head, expected):
        head = ListNode.from_array(head)
        actual = ListNode.mid_right(head)
        self.assertEqual(expected, actual.val if actual else None)

    def test_mid_left(self):
        self._test_mid_left([1, 2, 3], 2)
        self._test_mid_left([1, 2], 1)
        self._test_mid_left([], None)

    def _test_mid_left(self, head, expected):
        head = ListNode.from_array(head)
        actual = ListNode.mid_left(head)
        self.assertEqual(expected, actual.val if actual else None)


if __name__ == '__main__':
    unittest.main()
