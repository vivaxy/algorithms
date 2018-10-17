"""
https://leetcode.com/problems/partition-labels/

https://leetcode.com/submissions/detail/136359351/
"""


class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        currentFrom = 0
        currentTo = 0
        while currentTo < len(S):
            index = currentFrom
            while index <= currentTo:
                nextIndex = S.rfind(S[index], currentFrom)
                if nextIndex > currentTo:
                    currentTo = nextIndex
                index += 1
            result.append(currentTo - currentFrom + 1)
            currentFrom = currentTo + 1
            currentTo = currentFrom
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.partitionLabels(
            'ababcbacadefegdehijhklij'), [9, 7, 8])
        self.assertEqual(solution.partitionLabels('eaaaabaaec'), [9, 1])


if __name__ == '__main__':
    unittest.main()
