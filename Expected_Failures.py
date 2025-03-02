import unittest

class TestFailures(unittest.TestCase):
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1,6)

if __name__=="__main__":
    unittest.main()
