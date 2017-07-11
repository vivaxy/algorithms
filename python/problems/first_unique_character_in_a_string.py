"""
https://leetcode.com/problems/first-unique-character-in-a-string/

https://leetcode.com/submissions/detail/109165381/
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.firstUniqChar('leetcode'), 0)
        self.assertEqual(solution.firstUniqChar('loveleetcode'), 2)
        self.assertEqual(solution.firstUniqChar('cc'), -1)


if __name__ == '__main__':
    unittest.main()
