from concurrent.futures import ThreadPoolExecutor
import unittest

class TestParallel(unittest.TestCase):
    def test_task1(self):
        self.assertTrue(True)

    def test_task2(self):
        self.assertTrue(True)


if __name__=="__main__":
    with ThreadPoolExecutor() as executor:
        executor.submit(unittest.main)
