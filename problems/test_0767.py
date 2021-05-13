import collections
import unittest

import utils


# O(n) time. O(1) space. Hash table.
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s).most_common()
        max_ch, max_count = counts[0]

        if (max_count << 1) > len(s) + 1:
            return ''

        result = [None] * len(s)
        index = 0
        for i in range(max_count):
            result[index] = max_ch
            index += 2

        for i in range(1, len(counts)):
            ch, count = counts[i]
            for j in range(count):
                if index >= len(result):
                    index = 1
                result[index] = ch
                index += 2

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, expected, actual, msg, case):
        self.assertCountEqual(expected, actual, msg)

        for i in range(1, len(actual)):
            self.assertNotEqual(actual[i - 1], actual[i], msg)


if __name__ == '__main__':
    unittest.main()
