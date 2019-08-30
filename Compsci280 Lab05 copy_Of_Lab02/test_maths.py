import unittest     # Import the Python unit testing framework      # Our code to test
import maths
from maths import fibonacci


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #Arrange
        num1 = 6
        num2 = 4
        n = 16
        
        #Act
        act = maths.add(num1, num2)
        act2 = maths.add(num1, num2, n)
        
        #Assert
        self.assertEqual(act, '10')
        self.assertEqual(act2, "A")
    
    
        
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #Arrange
        test_number = 5
        fib_seq = [0,1,1,2,3,5,8,13,21,34, 55] #list of the first 10 values of the fibonacci sequence.
        
        #Act
        act = fibonacci(test_number)
        
        #Assert
        self.assertEqual(act, fib_seq[test_number])
    
    def test_convert_base(self):
        #Arrange
        num = 8
        n = 2
        num2 = 65535
        n2 = 16
        #Act
        act = maths.convert_base(num, n)
        act2 = maths.convert_base(num2, n2)
        
        #Assert
        self.assertEqual(act, "1000")
        self.assertEqual(act2, "FFFF")
    
    def test_factorial(self):
        test_number = 1
        
        act = factorial(1)
        
        self.assertEqual(act, 1) 
        
    


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
