import unittest
import work 
import test

class LocalTests(unittest.TestCase):
	def test_work(self):
		for case in test.cases:
			self.assertEqual(
				work.solution(*case[:-1]),
				case[-1:][0]
			)

if __name__ == '__main__':
	unittest.main()
