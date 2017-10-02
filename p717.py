import unittest


# O(n)
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        is_one_bit = False
        i = 0
        while i < len(bits):
            is_one_bit = not bits[i]
            i += 1 if is_one_bit else 2
        return is_one_bit


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 0, 0], True)
        self._test([1, 1, 1, 0], False)

    def _test(self, bits, expected):
        actual = Solution().isOneBitCharacter(bits)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
