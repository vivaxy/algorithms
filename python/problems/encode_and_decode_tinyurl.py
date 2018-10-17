"""
https://leetcode.com/problems/encode-and-decode-tinyurl/

https://leetcode.com/submissions/detail/131094266/
"""


class Codec:

    def encode(self, longUrl):
        """
        Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return longUrl

    def decode(self, shortUrl):
        """
        Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return shortUrl


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

import unittest


class Test(unittest.TestCase):
    def test(self):
        codec = Codec()
        url1 = 'https://leetcode.com'
        self.assertEqual(codec.decode(codec.encode(url1)), url1)


if __name__ == '__main__':
    unittest.main()
