import unittest
import solution

class TestSolution(unittest.TestCase):
	def test_solution(self):
		args = [
			10100101000001111010011100
		]
		output = 964176192 	
		self.assertEqual(solution.solution(*args), output)
		

if __name__ == '__main__':
	unittest.main()
