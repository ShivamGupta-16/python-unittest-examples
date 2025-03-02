import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        print("setUp called...")
        self.data = [1,2,3]

    def tearDown(self):
        print("tearDown called...")

    def test_list_length(self):
        self.assertEqual(len(self.data), 3)

    def test_list_content(self):
        self.assertIn(2, self.data)

if __name__ =="__main__":
    unittest.main()