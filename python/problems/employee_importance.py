"""
https://leetcode.com/problems/employee-importance/

https://leetcode.com/submissions/detail/129814911/
"""

# Employee info


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = dict()
        for employ in employees:
            dic[employ.id] = employ
        nextIds = [id]
        totalImportanceValue = 0
        while len(nextIds):
            nextEmployee = dic[nextIds.pop()]
            totalImportanceValue += nextEmployee.importance
            for sub in nextEmployee.subordinates:
                nextIds.append(sub)
        return totalImportanceValue


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        employee1 = Employee(1, 5, [2, 3])
        employee2 = Employee(2, 3, [])
        employee3 = Employee(3, 3, [])
        self.assertEqual(solution.getImportance(
            [employee1, employee2, employee3], 1), 11)


if __name__ == '__main__':
    unittest.main()
