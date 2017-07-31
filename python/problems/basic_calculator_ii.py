"""
https://leetcode.com/problems/basic-calculator-ii/

https://leetcode.com/submissions/detail/111848037/
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = []
        index = 0
        numbers = '0123456789'
        number = ''
        sign = '+'
        while index < len(s) + 1:
            if index < len(s) and s[index] in numbers:
                number += s[index]
                index += 1
                continue
            if number != '':
                if sign == '+':
                    array.append(int(number))
                elif sign == '-':
                    array.append(-int(number))
                elif sign == '*':
                    array.append(array.pop() * int(number))
                elif sign == '/':
                    prevNumber = array.pop()
                    if prevNumber < 0:
                        array.append(-int(-prevNumber / int(number)))
                    else:
                        array.append(int(prevNumber / int(number)))
                number = ''
            if index < len(s) and s[index] != ' ':
                sign = s[index]
            index += 1
        return sum(array)

    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        numbers = '0123456789'
        operators = '+-*/'
        liftedOperators = '*/'
        program = []
        while index < len(s):
            current = s[index]
            if current == ' ':
                index += 1
                continue
            if current in numbers:
                number = ''
                while index < len(s) and s[index] in numbers:
                    number += s[index]
                    index += 1
                program.append({'type': 'number', 'value': int(number)})
                continue
            if current in operators:
                program.append({'type': 'operator', 'value': current})
                index += 1
                continue
        i = 0
        while i < len(program):
            if program[i].get('type') == 'number':
                if i + 2 < len(program) and program[i + 1].get('value') in liftedOperators:
                    ope = program[i + 1].get('value')
                    if ope == '*':
                        token = {
                            'type': 'number',
                            'value': program[i].get('value') * program[i + 2].get('value')
                        }
                    else:
                        token = {
                            'type': 'number',
                            'value': int(program[i].get('value') / program[i + 2].get('value'))
                        }
                    program.pop(i)
                    program.pop(i)
                    program.pop(i)
                    program.insert(i, token)
                    continue
            i += 1
        while len(program) > 1:
            if program[1].get('value') == '+':
                token = {
                    'type': 'number',
                    'value': program[0].get('value') + program[2].get('value')
                }
            else:
                token = {
                    'type': 'number',
                    'value': program[0].get('value') - program[2].get('value')
                }
            program.pop(0)
            program.pop(0)
            program.pop(0)
            program.insert(0, token)
        return program[0].get('value')


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.calculate('14-3/2'), 13)
        self.assertEqual(solution.calculate('1-1+1'), 1)
        self.assertEqual(solution.calculate(' 3/2 '), 1)
        self.assertEqual(solution.calculate('0-2147483647'), -2147483647)
        self.assertEqual(solution.calculate('   30'), 30)
        self.assertEqual(solution.calculate('3+2*2'), 7)


if __name__ == '__main__':
    unittest.main()
