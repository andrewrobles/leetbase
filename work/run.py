import unittest
import work 
import test

class LocalTests(unittest.TestCase):
	def test_work(self):
		self.assertEqual(work.solution(*test.args), test.output)

if __name__ == '__main__':
	unittest.main()
