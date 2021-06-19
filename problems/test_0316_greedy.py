import unittest

import utils


def _find_max_possible_index(s, count, counts):
    counts = list(counts)
    for i in range(len(s) - 1, -1, -1):
        c = ord(s[i])
        if counts[c]:
            counts[c] = 0
            count -= 1
            if count == 0:
                return i


# O(n^2) time. O(1) space. Greedy.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        counts = [0] * (ord('z') + 1)

        for c in s:
            counts[ord(c)] = 1

        count = sum(counts)
        hi = _find_max_possible_index(s, count, counts)
        lo = 0

        for _ in range(count):
            min_c = 256
            min_i = 0
            for i in range(lo, hi + 1):
                c = ord(s[i])
                if counts[c] and c < min_c:
                    min_c = c
                    min_i = i

            result.append(chr(min_c))
            counts[min_c] = 0
            count -= 1
            lo = min_i + 1

            if min_c == ord(s[hi]):
                hi = _find_max_possible_index(s, count, counts)

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
