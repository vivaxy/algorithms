"""
https://leetcode.com/problems/reverse-string-ii/

https://leetcode.com/submissions/detail/111621414/
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        index = 0
        result = ''
        while index < len(s):
            if index % (2 * k) < k:
                # reverseÎ
                array = list(s[index:index + k])
                array.reverse()
                result += ''.join(array)
            else:
                # not reverse
                result += s[index:index + k]
            index += k
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.reverseStr('abcdefg', 2), 'bacdfeg')


if __name__ == '__main__':
    unittest.main()
