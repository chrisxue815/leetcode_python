import unittest

import utils

CHOICES = ''.join(
    [chr(ord('0') + i) for i in range(10)] +
    [chr(ord('A') + i) for i in range(26)] +
    [chr(ord('a') + i) for i in range(26)])

INDICES = [0] * 256
for i in range(10):
    INDICES[ord('0') + i] = i
for i in range(26):
    INDICES[ord('A') + i] = 10 + i
    INDICES[ord('a') + i] = 10 + 26 + i


class Codec:
    def __init__(self):
        self.long_urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        index = len(self.long_urls)
        self.long_urls.append(longUrl)

        short = []
        for _ in range(6):
            index, r = divmod(index, 62)
            short.append(CHOICES[r])

        return ''.join(short)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        index = 0
        power = 1

        for c in shortUrl:
            index += INDICES[ord(c)] * power
            power *= 62

        return self.long_urls[index]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            codec = Codec()
            actual = codec.decode(codec.encode(**case.args.__dict__))
            self.assertEqual(case.args.longUrl, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
