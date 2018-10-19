"""
https://leetcode.com/problems/keys-and-rooms/

https://leetcode.com/submissions/detail/183774624/
"""


class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = []

        def visit(roomId):
            if roomId in visited:
                return
            visited.append(roomId)
            for id in rooms[roomId]:
                visit(id)
        visit(0)
        return len(visited) == len(rooms)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.canVisitAllRooms([[1], [2], [3], []]), True)


if __name__ == '__main__':
    unittest.main()
