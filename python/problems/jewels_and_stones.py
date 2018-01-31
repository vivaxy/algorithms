"""
https://leetcode.com/problems/jewels-and-stones/description/

https://leetcode.com/submissions/detail/138688434/
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for stone in J:
            result += S.count(stone)
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones('aA', 'aAAbbbb'), 3)
        self.assertEqual(solution.numJewelsInStones('z', 'ZZ'), 0)


if __name__ == '__main__':
    unittest.main()
