import unittest
import utils


def bit_count(x):
    # Hacker's Delight, Figure 5-2
    # OpenJDK:
    # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/Integer.java#1082
    x = x - ((x >> 1) & 0x55555555)  # (xx & 01) + ((xx >> 1) & 01) == xx - ((xx >> 1) & 01)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f
    x += x >> 8
    x += x >> 16
    return x & 0x3f


# O(n * log(sizeof(integer))) time. O(1) space. Bit count.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bit_count(x) for x in xrange(num + 1)]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p338.json').test_cases

        for case in cases:
            actual = Solution().countBits(case.num)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
