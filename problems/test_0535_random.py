import random
import unittest

import utils

CHOICES = ''.join(
    [chr(ord('0') + i) for i in range(10)] +
    [chr(ord('A') + i) for i in range(26)] +
    [chr(ord('a') + i) for i in range(26)])


class Codec:
    def __init__(self):
        self.short_to_long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while True:
            short = []
            for _ in range(6):
                short.append(random.choice(CHOICES))
            short = ''.join(short)

            if short not in self.short_to_long:
                self.short_to_long[short] = longUrl
                return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.short_to_long[shortUrl]


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
