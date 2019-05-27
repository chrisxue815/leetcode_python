import unittest


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        slen = len(s)
        # [0,p1) [p1,p2) [p2,p3) [p3,slen)
        for p1 in range(max(1, slen - 9), min(4, slen - 2)):
            if p1 > 1 and s[0] == '0':
                break
            for p2 in range(max(p1 + 1, slen - 6), min(p1 + 4, slen - 1)):
                if p2 - p1 > 1 and s[p1] == '0':
                    break
                for p3 in range(max(p2 + 1, slen - 3), min(p2 + 4, slen)):
                    if p3 - p2 > 1 and s[p2] == '0':
                        break
                    if slen - p3 > 1 and s[p3] == '0':
                        continue
                    s1 = s[0:p1]
                    if int(s1) > 255:
                        continue
                    s2 = s[p1:p2]
                    if int(s2) > 255:
                        continue
                    s3 = s[p2:p3]
                    if int(s3) > 255:
                        continue
                    s4 = s[p3:slen]
                    if int(s4) > 255:
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
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
