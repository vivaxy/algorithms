"""
https://leetcode.com/problems/1-bit-and-2-bit-characters/

https://leetcode.com/submissions/detail/130474783/
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        """
        找规律：去掉最后一个 0，再找到最后一个 0 字符的位置，看中间有几个 1，如果是奇数，则 False，如果是偶数，则 True
        """
        bits.pop()
        oneCount = 0
        while len(bits) and bits.pop() == 1:
            oneCount += 1
        return oneCount % 2 == 0


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.isOneBitCharacter([1, 0, 0]), True)
        self.assertEqual(solution.isOneBitCharacter([1, 1, 1, 0]), False)


if __name__ == '__main__':
    unittest.main()
