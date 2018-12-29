import unittest


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        path_len = indent = 0
        lo = prev_indent = -1
        max_len = 1
        is_file = False
        stack = []

        for hi in xrange(len(input) + 1):
            if hi == len(input) or input[hi] == '\n':
                for _ in xrange(prev_indent - indent + 1):
                    path_len -= stack.pop()

                curr_len = hi - lo
                path_len += curr_len
                stack.append(curr_len)

                if is_file and path_len > max_len:
                    max_len = path_len

                lo = hi
                prev_indent = indent
                indent = 0
                is_file = False
            elif input[hi] == '\t':
                lo = hi
                indent += 1
            elif input[hi] == '.':
                is_file = True

        return max_len - 1


class Test(unittest.TestCase):
    def test(self):
        self._test('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext', 20)
        self._test('dir\n\tsubdir1\n\tsubdir2\n\t\tfile', 0)
        self._test('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext', 32)

    def _test(self, input, expected):
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
