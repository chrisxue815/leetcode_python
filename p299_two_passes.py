import unittest
import collections


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        counter = collections.Counter(secret)
        for i, digit in enumerate(guess):
            if digit == secret[i]:
                bulls += 1
                if counter[digit]:
                    counter[digit] -= 1
                else:
                    cows -= 1
            elif counter[digit]:
                cows += 1
                counter[digit] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'


class Test(unittest.TestCase):
    def test(self):
        self._test('1807', '7810', '1A3B')
        self._test('1123', '0111', '1A1B')
        self._test('1122', '1222', '3A0B')

    def _test(self, secret, guess, expected):
        actual = Solution().getHint(secret, guess)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
