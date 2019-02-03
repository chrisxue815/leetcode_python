import unittest


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        slen = len(s)
        # [0,p1) [p1,p2) [p2,p3) [p3,slen)
        for p1 in range(1, 4):
            for p2 in range(p1 + 1, p1 + 4):
                for p3 in range(p2 + 1, p2 + 4):
                    l4 = slen - p3
                    if l4 < 1 or l4 > 3:
                        continue
                    if p1 > 1 and s[0] == '0':
                        continue
                    l2 = p2 - p1
                    if l2 > 1 and s[p1] == '0':
                        continue
                    l3 = p3 - p2
                    if l3 > 1 and s[p2] == '0':
                        continue
                    if l4 > 1 and s[p3] == '0':
                        continue
                    s1 = s[0:p1]
                    b1 = int(s1)
                    if b1 > 255:
                        continue
                    s2 = s[p1:p2]
                    b2 = int(s2)
                    if b2 > 255:
                        continue
                    s3 = s[p2:p3]
                    b3 = int(s3)
                    if b3 > 255:
                        continue
                    s4 = s[p3:slen]
                    b4 = int(s4)
                    if b4 > 255:
                        continue
                    result.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test('25525511135', [
            '255.255.11.135',
            '255.255.111.35',
        ])

        self._test('10999', [
            '10.9.9.9',
            '1.0.99.9',
            '1.0.9.99',
            # Should not contain 1.9.9.9
        ])

    def _test(self, s, expected):
        actual = Solution().restoreIpAddresses(s)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
