"""
https://leetcode.com/problems/combination-sum-iii/

https://leetcode.com/submissions/detail/111503972/
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = list(range(1, 10))
        answers = []

        def traverse(cand, current, k, n):
            if k == 1:
                if n in cand:
                    sortedCurrent = sorted(current + [n])
                    if not sortedCurrent in answers:
                        answers.append(sortedCurrent)
                return
            for one in cand:
                nextCand = cand[:]
                nextCand.remove(one)
                traverse(nextCand, current + [one], k - 1, n - one)
        traverse(candidates, [], k, n)
        return answers


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.combinationSum3(3, 7), [[1, 2, 4]])


if __name__ == '__main__':
    unittest.main()
