import unittest

class TestSkipping(unittest.TestCase):
    @unittest.skip("Skipping this test")
    def test_skip_example(self):
        self.assertEqual(1,1)

if __name__ =="__main__":
    unittest.main()