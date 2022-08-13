import unittest
import work 

class LocalTests(unittest.TestCase):
	def test_work(self):
		for test in work.tests:
			self.assertEqual(
				work.solution(*test['args']),
				test['output']
			)

if __name__ == '__main__':
	unittest.main()
