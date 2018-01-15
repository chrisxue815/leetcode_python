import unittest


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        path_lengths = {0: 0}

        for seg in input.split('\n'):
            name = seg.lstrip('\t')
            depth = len(seg) - len(name)

            if '.' in name:
                max_len = max(max_len, path_lengths[depth] + len(name))
            else:
                path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1

        return max_len


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
