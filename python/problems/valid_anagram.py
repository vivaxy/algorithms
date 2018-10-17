"""
https://leetcode.com/problems/valid-anagram/

https://leetcode.com/submissions/detail/130841292/
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = dict()
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        dic2 = dict()
        for char in t:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1
        return dic == dic2


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.isAnagram('anagram', 'nagaram'), True)
        self.assertEqual(solution.isAnagram('rat', 'car'), False)


if __name__ == '__main__':
    unittest.main()
