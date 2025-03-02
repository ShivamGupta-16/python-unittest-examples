'''
In unittest, assertions are methods used to check whether a certain condition holds true during testing. If the assertion fails (i.e., the condition is false), the test case fails.

***Here are some frequently used assertion methods in the unittest module:***

*assertEqual(a, b) – Checks if a == b
*assertNotEqual(a, b) – Checks if a != b
*assertTrue(x) – Checks if x is True
*assertFalse(x) – Checks if x is False
*assertIs(a, b) – Checks if a is b (same object in memory)
*assertIsNot(a, b) – Checks if a is not b
*assertIsNone(x) – Checks if x is None
*assertIsNotNone(x) – Checks if x is not None
*assertIn(a, b) – Checks if a is in b
*assertNotIn(a, b) – Checks if a is not in b
*assertRaises(Exception, function, *args, **kwargs) – Checks if calling function(*args, **kwargs) raises the expected Exception.
'''


import unittest

def add(x,y):
    return x+y

class TestCacl(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,6),7)
        self.assertNotEqual(add(1,6), 8)
        self.assertTrue(add(1,3)==4)
        self.assertFalse(add(1,3)==5)

if __name__ =="__main__":
    unittest.main()