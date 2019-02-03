import unittest
from linkedlist import ListNode


class Solution(object):
    def getIntersectionNode(self, a, b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def list_len(x):
            result = 0
            while x:
                x = x.next
                result += 1
            return result

        a_len = list_len(a)
        b_len = list_len(b)

        if a_len > b_len:
            for _ in range(a_len - b_len):
                a = a.next
        else:
            for _ in range(b_len - a_len):
                b = b.next

        while a is not b:
            a = a.next
            b = b.next

        return a


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 3, 4], [5, 6, 7], 2)

    def _test(self, a, b_before_intersection, a_len_before_intersection):
        a = ListNode.from_array(a)
        b = ListNode.from_array(b_before_intersection)

        intersection = a
        for _ in range(a_len_before_intersection):
            intersection = intersection.next

        b_end = b
        while b_end.next:
            b_end = b_end.next

        b_end.next = intersection

        actual = Solution().getIntersectionNode(a, b)
        self.assertEqual(intersection, actual)


if __name__ == '__main__':
    unittest.main()
