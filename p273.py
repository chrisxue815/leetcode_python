import unittest

_digits = [
    '',
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
]

_ten_sth = [
    'Ten',
    'Eleven',
    'Twelve',
    'Thirteen',
    'Fourteen',
    'Fifteen',
    'Sixteen',
    'Seventeen',
    'Eighteen',
    'Nineteen',
]

_tens = [
    '',
    '',
    'Twenty',
    'Thirty',
    'Forty',
    'Fifty',
    'Sixty',
    'Seventy',
    'Eighty',
    'Ninety',
]


def _to_words(words, nums):
    before_len = len(words)

    if nums[2] > 0:
        words.append(_digits[nums[2]])
        words.append('Hundred')

    if nums[1] == 1:
        words.append(_ten_sth[nums[0]])
    else:
        if nums[1] != 0:
            words.append(_tens[nums[1]])
        if nums[0] != 0:
            words.append(_digits[nums[0]])

    return before_len != len(words)


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        words = []
        nums = [0] * 12
        i = 0
        while num > 0:
            num, nums[i] = divmod(num, 10)
            i += 1

        if _to_words(words, nums[9:]):
            words.append('Billion')

        if _to_words(words, nums[6:9]):
            words.append('Million')

        if _to_words(words, nums[3:6]):
            words.append('Thousand')

        _to_words(words, nums[:3])

        return ' '.join(words)


class Test(unittest.TestCase):
    def test(self):
        self._test(123, 'One Hundred Twenty Three')
        self._test(12345, 'Twelve Thousand Three Hundred Forty Five')
        self._test(1234567, 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')
        self._test(0, 'Zero')
        self._test(10000000, 'Ten Million')
        self._test(10000001, 'Ten Million One')

    def _test(self, num, expected):
        actual = Solution().numberToWords(num)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
