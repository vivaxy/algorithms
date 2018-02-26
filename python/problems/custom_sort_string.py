"""
https://leetcode.com/problems/custom-sort-string/description/

https://leetcode.com/submissions/detail/142301270/
https://leetcode.com/submissions/detail/142463607/
"""


from functools import cmp_to_key


class Solution1:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def compare(x, y):
            return S.find(x) - S.find(y)
        return ''.join(sorted(list(T), key=cmp_to_key(compare)))


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def quickSort(array, start, end):
            i = start
            j = end
            while i < j:
                while i < j and S.find(array[i]) <= S.find(array[j]):
                    j -= 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                while i < j and S.find(array[i]) < S.find(array[j]):
                    i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
            if start < i - 1:
                quickSort(array, start, i - 1)
            if end > i + 1:
                quickSort(array, i + 1, end)
        ans = list(T)
        quickSort(ans, 0, len(ans) - 1)
        return ''.join(ans)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.customSortString('cba', 'abcd'), 'dcba')


if __name__ == '__main__':
    unittest.main()
