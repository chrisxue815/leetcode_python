import unittest


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self._backtrack(s, result, [], 0)
        return result

    def _backtrack(self, s, result, ip, lo):
        if len(ip) < 4:
            if lo >= len(s):
                return

            hi_start = max(lo + 1, len(s) + len(ip) - 10)

            if s[lo] == '0':
                hi_end = hi_start + 1
            else:
                hi_end = min(lo + 4, len(s) + 1)

            for hi in range(hi_start, hi_end):
                byte = int(s[lo:hi])
                if byte >= 256:
                    continue

                ip.append(byte)
                self._backtrack(s, result, ip, hi)
                ip.pop()

        elif len(ip) == 4 and lo == len(s):
            ip_str = '.'.join(str(byte) for byte in ip)
            result.append(ip_str)


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
