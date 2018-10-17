"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

https://leetcode.com/submissions/detail/143826044/
"""


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findMaximumXOR([3, 10, 5, 25, 2, 8]), 28)


if __name__ == '__main__':
    unittest.main()
