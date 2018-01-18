import unittest


def check_ipv4(ip):
    def valid_part(part):
        if not part or part[0] == '-' or len(part) > 1 and part[0] == '0':
            return False
        try:
            return int(part) < 256
        except ValueError:
            return False

    parts = ip.split('.')
    return len(parts) == 4 and all(valid_part(part) for part in parts)


def check_ipv6(ip):
    def valid_part(part):
        if not part or part[0] == '-' or len(part) > 4:
            return False
        try:
            return int(part, 16) < 65536
        except ValueError:
            return False

    parts = ip.split(':')
    return len(parts) == 8 and all(valid_part(part) for part in parts)


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        n = len(IP)
        if n > 15 or n == 15 and IP[1] == ':':
            return 'IPv6' if check_ipv6(IP) else 'Neither'
        else:
            return 'IPv4' if check_ipv4(IP) else 'Neither'


class Test(unittest.TestCase):
    def test(self):
        self._test('172.16.254.1', 'IPv4')
        self._test('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6')
        self._test('256.256.256.256', 'Neither')
        self._test('0:0:0:0:0:0:0:0', 'IPv6')
        self._test('01.0.0.0', 'Neither')
        self._test('-1.0.0.0', 'Neither')
        self._test('-0.0.0.0', 'Neither')
        self._test('00000:0:0:0:0:0:0:0', 'Neither')
        self._test('-1:0:0:0:0:0:0:0', 'Neither')
        self._test('-0:0:0:0:0:0:0:0', 'Neither')

    def _test(self, IP, expected):
        actual = Solution().validIPAddress(IP)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
