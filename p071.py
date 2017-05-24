import unittest


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        n = len(path)
        stack = []
        lo = 1
        i = 1

        while i <= n:
            if i == n or path[i] == '/':
                part = path[lo:i]
                if part == '..':
                    if stack:
                        stack.pop()
                elif part and part != '.':
                    stack.append(part)
                lo = i + 1
            i += 1

        return '/' + '/'.join(stack)


class Test(unittest.TestCase):
    def test(self):
        self._test('/home/', '/home')
        self._test('/a/./b/../../c/', '/c')
        self._test('/../a/./b/../..//c/', '/c')
        self._test('/', '/')

    def _test(self, path, expected):
        actual = Solution().simplifyPath(path)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
