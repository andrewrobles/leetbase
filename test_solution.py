import unittest
import solution

class TestSolution(unittest.TestCase):
	def test_solution(self):
		for test in solution.tests:
			print('running test')
			self.assertEqual(
				solution.solution(*test['args']),
				test['output']
			)
		self.assertEqual(solution.solution(*args), output)
		

if __name__ == '__main__':
	unittest.main()
