import unittest

#Function to be tested

def add(x,y):
    return x+y

class TestCalc(unittest.TestCase):
# test keyword (test_add) is mandatory to be written as prefix of the function name. Only self parameter can be passed
    def test_add(self):
        self.assertEqual(add(1,6), 7) #Test passes
        self.assertEqual(add(3,5), 8) #passes
        self.assertEqual(add(3,4), 9) #didn't passes 

if __name__ =="__main__":
    unittest.main()