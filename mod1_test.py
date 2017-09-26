import unittest
class ForTwitter(unittest.TestCase):
	def setUp(self):
		print ('hello testing travis')
	def leaving(self):
		print ('Exiting Travis')
if __name__ == "__main__":
	unittest.main()
	print('hello')
