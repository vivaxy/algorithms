"""
https://leetcode.com/problems/find-anagram-mappings/description/

https://leetcode.com/submissions/detail/135434308/
"""


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        P = []
        for a in A:
            i = B.index(a)
            P.append(i)
        return P


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.anagramMappings(
            [12, 28, 46, 32, 50], [50, 12, 32, 46, 28]), [1, 4, 3, 2, 0])


if __name__ == '__main__':
    unittest.main()
