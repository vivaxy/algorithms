"""
https://leetcode.com/problems/beautiful-arrangement-ii/description/

https://leetcode.com/submissions/detail/131456129/
"""


class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        """
        n = 4
        k = 2
        ---
        [4, 3, 1, 2]
         ^  ^
         两位从尾部开始，位数和 n - k 的值相等
               ^  ^
               剩下的从剩余的数组的头部取/尾部取/头部取...
        """
        result = []
        l = list(range(1, n + 1))
        t = n - k
        while t > 0:
            result.append(l.pop())
            t -= 1
        flag = True
        while len(l):
            if flag:
                result.append(l.pop(0))
            else:
                result.append(l.pop())
            flag = not flag
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.constructArray(3, 1), [3, 2, 1])
        self.assertEqual(solution.constructArray(3, 2), [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
