import unittest

class TestDemo(unittest.TestCase):
    def test_example(self):
        self. assertTrue(True)


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)