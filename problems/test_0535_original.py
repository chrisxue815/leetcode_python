import unittest

import utils


class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return longUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return shortUrl


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
