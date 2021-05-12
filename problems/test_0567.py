import unittest

import utils


# O(n) time. O(1) space. Sliding window.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lo = 0
        target = len(s1) - 1
        counts = [0] * 128
        for c in s1:
            counts[ord(c)] += 1

        for hi, c in enumerate(s2):
            c = ord(c)
            count = counts[c]

            if count == 0:
                while True:
                    lo_char = ord(s2[lo])
                    lo += 1
                    if lo_char == c:
                        break
                    counts[lo_char] += 1
            else:
                count -= 1
                if count == 0 and hi - lo == target:
                    return True
                counts[c] = count

        return False


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
