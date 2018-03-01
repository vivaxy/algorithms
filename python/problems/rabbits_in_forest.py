"""
https://leetcode.com/problems/rabbits-in-forest/description/

https://leetcode.com/submissions/detail/142931373/
"""

import math

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic = dict()
        for answer in answers:
            if answer in dic:
                dic[answer] += 1
            else:
                dic[answer] = 1
        ans = 0
        for answer in dic:
            ans += math.ceil(dic[answer] / (answer + 1)) * (answer + 1)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numRabbits([0, 0, 1, 1, 1]), 6)
        self.assertEqual(solution.numRabbits([1, 0, 1, 0, 0]), 5)
        self.assertEqual(solution.numRabbits([]), 0)
        self.assertEqual(solution.numRabbits([1, 1, 2]), 5)
        self.assertEqual(solution.numRabbits([10, 10, 10]), 11)


if __name__ == '__main__':
    unittest.main()
