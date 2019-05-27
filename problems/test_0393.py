import unittest


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        size = len(data)
        i = 0
        while i < size:
            lead = data[i]
            if not lead >> 7:
                i += 1
                continue
            elif lead >> 5 == 0b110:
                n = 2
            elif lead >> 4 == 0b1110:
                n = 3
            elif lead >> 3 == 0b11110:
                n = 4
            else:
                return False
            hi = i + n
            if hi > size:
                return False
            i += 1
            while i < hi:
                if data[i] >> 6 != 0b10:
                    return False
                i += 1
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([197, 130, 1], True)
        self._test([235, 140, 4], False)
        self._test([230, 136, 145], True)
        self._test([145], False)

    def _test(self, data, expected):
        actual = Solution().validUtf8(data)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
