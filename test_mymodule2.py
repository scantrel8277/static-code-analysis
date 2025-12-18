# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'add' functions from the 'mymodule2' module.
from mymodule2 import add

# Define a test case class for testing the 'add' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestAdd(unittest.TestCase): 

    # Define the first test method for the 'add' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'add(2, 4)' returns 6.
        # This tests if the function correctly computes the sum of 2 and 4.
        self.assertEqual(add(2, 4), 6) # test when 2 and 4 are given as input the output is 6.

        # Check that calling 'add(0, 0)' returns 0.
        # This tests if the function correctly computes the sum of 0 and 0.
        self.assertEqual(add(0, 0), 0)  # test when 0 and 0 are given as input the output is 0.

        # Check that calling 'add(2.3, 3.6)' returns 5.9.
        # This tests if the function correctly computes the sum of 2.3 and 3.6.
        self.assertEqual(add(2.3, 3.6), 5.9)  # test when 2.3 and 3.6 are given as input the output is 5.9.

        # Check that calling 'add('hello', 'world')' returns 'helloworld'.
        # This tests if the function correctly computes the sum of 'hello' and 'world'.
        self.assertEqual(add('hello', 'world'), 'helloworld') # test when 'hello' and 'world' are given as input the output is 'helloworld'.

        # Check that calling 'add(2.3000, 4.300)' returns 6.6.
        # This tests if the function correctly computes the sum of 2.3000 and 4.300.
        self.assertEqual(add(2.3000, 4.300), 6.6) # test when 2.3000 and 4.300 are given as input the output is 6.6.

        # Check that calling 'add(-2, -2)' does not return 0.
        # This tests if the function correctly computes the sum of -2 and -2.
        self.assertNotEqual(add(-2, -2), 0) # test when -2 and -2 are given as input the output is not 0.
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
