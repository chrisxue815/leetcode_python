import unittest


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)

        return '/' + '/'.join(stack)


class Test(unittest.TestCase):
    def test(self):
        self._test('/home/', '/home')
        self._test('/a/./b/../../c/', '/c')
        self._test('/../a/./b/../..//c/', '/c')
        self._test('/', '/')

    def _test(self, path, expected):
        actual = Solution().simplifyPath(path)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
