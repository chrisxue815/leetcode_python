import unittest

import utils


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    @staticmethod
    def decode(vals):
        dummy = Node(0, None, None, None)
        prev = dummy

        for val in vals:
            if isinstance(val, list):
                prev.child = Node.decode(val)
            else:
                curr = Node(val, prev, None, None)
                prev.next = curr

        return dummy.next

    @staticmethod
    def encode(head):
        result = []
        curr = head

        while curr:
            result.append(curr.val)
            if curr.child:
                result.append(Node.encode(curr.child))
            curr = curr.next

        return result

    @staticmethod
    def assert_equal(t, expected, actual, msg):
        while expected and actual:
            t.assertEqual(expected.val, actual.val, msg=msg)
            t.assertEqual(expected.prev.val if expected.prev else None, actual.prev.val if actual.prev else None, msg=msg)
            Node.assert_equal(t, expected.child, actual.child, msg=msg)
            expected = expected.next
            actual = actual.next
        t.assertEqual(expected is None, actual is None, msg=msg)


def flatten(head):
    curr = head
    prev = head

    while curr:
        if curr.child:
            child = curr.child
            curr.child = None

            tail = flatten(child)

            nxt = curr.next
            curr.next = child
            child.prev = curr

            if nxt:
                tail.next = nxt
                nxt.prev = tail

            prev = tail
            curr = nxt
        else:
            prev = curr
            curr = curr.next

    return prev


# O(n) time. O(depth) space. Lined list.
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        flatten(head)
        return head


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            utils.solve_references(case.args.head)
            utils.solve_references(case.expected)

            args = str(case.args)
            actual = Solution().flatten(**case.args.__dict__)

            self.assertEqual(Node.encode(case.expected), Node.encode(actual), msg=args)
            Node.assert_equal(self, case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
