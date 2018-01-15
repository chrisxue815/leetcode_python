import unittest


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
        self._test('https://leetcode.com/problems/design-tinyurl')

    def _test(self, url):
        codec = Codec()
        self.assertEqual(url, codec.decode(codec.encode(url)))


if __name__ == '__main__':
    unittest.main()
