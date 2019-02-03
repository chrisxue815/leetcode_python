import unittest


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        last = 0
        result = [last]
        visited = set(result)
        while True:
            for i in range(n):
                curr = last ^ (1 << i)
                if curr not in visited:
                    visited.add(curr)
                    result.append(curr)
                    last = curr
                    break
            else:
                return result


class Test(unittest.TestCase):
    def test(self):
        self._test(0, [0])
        self._test(1, [0, 1])
        self._test(2, [0, 1, 3, 2])

    def _test(self, n, expected):
        actual = Solution().grayCode(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
