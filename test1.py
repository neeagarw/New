import unittest
from hello import hello1
  
class myTest(unittest.TestCase):
	def test_default_greeting_set(self):
		hello1 = hello1()
		self.assertEqual(greeter.message,'Hello world')
if __name__ == '__main__':
  unittest.main()
