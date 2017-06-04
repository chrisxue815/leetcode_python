import unittest


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        size = len(data)
        i = 0
        while i < size:
            lead = data[i]
            if not lead & 0x80:
                i += 1
                continue
            elif lead & 0xe0 == 0xc0:
                n = 2
            elif lead & 0xf0 == 0xe0:
                n = 3
            elif lead & 0xf8 == 0xf0:
                n = 4
            else:
                return False
            hi = i + n
            if hi > size:
                return False
            i += 1
            while i < hi:
                if data[i] & 0xc0 != 0x80:
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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
