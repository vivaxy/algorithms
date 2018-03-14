"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/

https://leetcode.com/submissions/detail/145027866/
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        dest = len(graph) - 1
        ans = []

        def dfs(currentNode, path):
            if currentNode == dest:
                ans.append(path)
                return
            possiblePaths = graph[currentNode]
            for p in possiblePaths:
                dfs(p, path + [p])
        dfs(0, [0])
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.allPathsSourceTarget(
            [[1, 2], [3], [3], []]), [[0, 1, 3], [0, 2, 3]])


if __name__ == '__main__':
    unittest.main()
