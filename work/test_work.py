import unittest
import work 

class LocalTests(unittest.TestCase):
	def test_work(self):
		for test in work.tests:
			self.assertEqual(
				work.solution(*test[:-1]),
				test[-1:][0]
			)

if __name__ == '__main__':
	unittest.main()
