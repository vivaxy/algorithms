"""
https://leetcode.com/problems/delete-operation-for-two-strings/

https://leetcode.com/submissions/detail/117292466/
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix = [list(range(len(word1) + 1))]
        for i in range(1, len(word2) + 1):
            row = [i]
            for j in range(1, len(word1) + 1):
                insert = row[j - 1] + 1
                delete = matrix[i - 1][j] + 1
                remaing = matrix[i - 1][j - 1]
                # 如果两个字符不想等，则相当于删除了两个字符
                diff = 0 if word2[i - 1] == word1[j - 1] else 2
                nextValue = min(insert, delete, remaing + diff)
                row.append(nextValue)
            matrix.append(row)
        return matrix[len(word2)][len(word1)]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minDistance('sea', 'eat'), 2)
        self.assertEqual(solution.minDistance('a', 'b'), 2)


if __name__ == '__main__':
    unittest.main()
