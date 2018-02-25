"""
https://leetcode.com/problems/custom-sort-string/description/

https://leetcode.com/submissions/detail/142301270/
"""


from functools import cmp_to_key


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def compare(x, y):
            return S.find(x) - S.find(y)
        return ''.join(sorted(list(T), key=cmp_to_key(compare)))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.customSortString('cba', 'abcd'), 'dcba')


if __name__ == '__main__':
    unittest.main()
