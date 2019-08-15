import bisect
import unittest
from typing import List

import utils


class SortedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def __setitem__(self, key, value):
        i = bisect.bisect_left(self._keys, key)
        if i < len(self._keys) and self._keys[i] == key:
            self._keys[i] = key
            self._values[i] = value
        else:
            self._keys.insert(i, key)
            self._values.insert(i, value)

    def find_ge(self, key, default=(None, None)):
        i = bisect.bisect_left(self._keys, key)
        if i < len(self._keys):
            return self._keys[i], self._values[i]
        else:
            return default

    def find_le(self, key, default=(None, None)):
        i = bisect.bisect_right(self._keys, key)
        if i:
            return self._keys[i - 1], self._values[i - 1]
        else:
            return default


# O(nlog(n)) time. O(n) space. Sorted map, DP.
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        result = 1

        num_to_index = SortedDict()
        num_to_index[A[-1]] = n - 1

        up = [False] * n
        down = [False] * n
        up[-1] = down[-1] = True

        for i in range(n - 2, -1, -1):
            ai = A[i]

            aj, j = num_to_index.find_ge(ai)
            if j is not None:
                up[i] = down[j]
                if up[i]:
                    result += 1

            aj, j = num_to_index.find_le(ai)
            if j is not None:
                down[i] = up[j]

            num_to_index[ai] = i

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().oddEvenJumps(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
