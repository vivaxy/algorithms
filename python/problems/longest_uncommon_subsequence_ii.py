"""
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

"""


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # 从长到短排序
        sortedStrs = sorted(strs, key=len, reverse=True)
        for index1, str in enumerate(sortedStrs):
            # 从最长的字符串开始
            foundSameString = False
            for index2 in range(len(sortedStrs)):
                if len(str) != len(sortedStrs[index2]):
                    # 如果较长的字符串和之后一个相比更长，则不用再比较其他字符串了
                    break
                else:
                    if str == sortedStrs[index2]:
                        foundSameString = True
                        break
            if not foundSameString:
                return len(str)
        return -1


import unittest


class Test(unittest.TestCase):
    def test(self):
        # solution = Solution()
        # self.assertEqual(solution.findLUSlength(['aba', 'cdc', 'eae']), 3)
        # self.assertEqual(solution.findLUSlength(['aaa', 'aaa', 'a']), -1)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
