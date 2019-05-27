import unittest
import heapq


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        n -= 2
        q = [(primes[0], 0)]

        for _ in range(n):
            curr, i = q[0]
            heapq.heapreplace(q, (curr * primes[i], i))
            if i + 1 < len(primes):
                heapq.heappush(q, (curr // primes[i] * primes[i + 1], i + 1))

        return q[0][0]


class Test(unittest.TestCase):
    def test(self):
        self._test(1, [2, 7, 13, 19], 1)
        self._test(2, [2, 7, 13, 19], 2)  # 2
        self._test(3, [2, 7, 13, 19], 4)  # 2 * 2
        self._test(4, [2, 7, 13, 19], 7)  # 7
        self._test(5, [2, 7, 13, 19], 8)  # 2 * 2 * 2
        self._test(6, [2, 7, 13, 19], 13)  # 13
        self._test(7, [2, 7, 13, 19], 14)  # 2 * 7
        self._test(8, [2, 7, 13, 19], 16)  # 2 * 2 * 2 * 2
        self._test(9, [2, 7, 13, 19], 19)  # 19
        self._test(10, [2, 7, 13, 19], 26)  # 2 * 13
        self._test(11, [2, 7, 13, 19], 28)  # 2 * 19
        self._test(12, [2, 7, 13, 19], 32)  # 2 * 2 * 2 * 2 * 2

    def _test(self, n, primes, expected):
        actual = Solution().nthSuperUglyNumber(n, primes)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
