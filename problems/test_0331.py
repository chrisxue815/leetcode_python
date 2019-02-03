import unittest


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        n = len(preorder)
        leaves = 1
        i = 0
        while i < n:
            ch = preorder[i]
            if ch == '#':
                leaves -= 1
                if leaves < 0:
                    return False
                i += 2
                if leaves == 0 and i < n:
                    return False
            else:
                leaves += 1
                i += 1
                while i < n and preorder[i] != ',':
                    i += 1
                i += 1
        return leaves == 0


class Test(unittest.TestCase):
    def test(self):
        self._test('9,3,4,#,#,1,#,#,2,#,6,#,#', True)
        self._test('1,#', False)
        self._test('9,#,#,1', False)
        self._test('#', True)
        self._test('#,1,#', False)

    def _test(self, preorder, expected):
        actual = Solution().isValidSerialization(preorder)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
