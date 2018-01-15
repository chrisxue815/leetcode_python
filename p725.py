import unittest
from linkedlist import ListNode


def get_count(root):
    count = 0
    while root:
        root = root.next
        count += 1
    return count


# O(n). Math.
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = [None] * k
        count = get_count(root)
        small_chunk_size, num_large_chunks = divmod(count, k)

        for i in xrange(num_large_chunks):
            result[i] = root
            for j in xrange(small_chunk_size):
                root = root.next
            new_root = root.next
            root.next = None
            root = new_root

        small_chunk_size -= 1
        for i in xrange(num_large_chunks, k):
            result[i] = root
            for j in xrange(small_chunk_size):
                root = root.next
            if root:
                new_root = root.next
                root.next = None
                root = new_root

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 5, [[1], [2], [3], [], []])
        self._test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])

    def _test(self, root, k, expected):
        root = ListNode.from_array(root)

        actual = Solution().splitListToParts(root, k)

        actual = [ListNode.to_array(node) for node in actual]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
