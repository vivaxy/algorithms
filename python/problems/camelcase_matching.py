import unittest
"""
https://leetcode.com/problems/camelcase-matching/

https://leetcode.com/submissions/detail/221432714/
"""

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def testQuery(query: str, pattern: str) -> bool:
            if len(pattern):
                if len(query):
                    i = query.find(pattern[0])
                    if i == -1:
                        return False
                    if query[:i].lower() != query[:i]:
                        return False
                    return testQuery(query[i + 1:], pattern[1:])
                return False
            return query.lower() == query
        return list(map(lambda query: testQuery(query, pattern), queries))


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.camelMatch(
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], 'FB'),
            [True, False, True, True, False]
        )
        self.assertEqual(solution.camelMatch(
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], 'FoBa'),
            [True, False, True, False, False]
        )
        self.assertEqual(solution.camelMatch(
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], 'FoBaT'),
            [False, True, False, False, False]
        )
        self.assertEqual(solution.camelMatch(
            ["IXfGawluvnCa", "IsXfGaxwulCa", "IXfGawlqtCva",
                "IXjfGawlmeCa", "IXfGnaynwlCa", "IXfGcamwelCa"], "IXfGawlCa"),
            [True, True, True, True, True, True])


if __name__ == '__main__':
    unittest.main()
