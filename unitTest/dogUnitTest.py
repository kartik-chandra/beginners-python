import unittest
import sys
import os

# Add the path to the 'basic' folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'basic'))

from Dog import Dog 

class TestDogClass(unittest.TestCase):

    def setUp(self):
        # Create an instance of Dog for testing
        self.dog = Dog(name="Buddy", age=3)

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_bark(self):
        expected_output = "GHAUUUU ... Buddy is barking"
        with unittest.mock.patch('builtins.print', side_effect=print) as mock_print:
            self.dog.bark()
            mock_print.assert_called_once_with(expected_output)

    def test_roll_over(self):
        expected_output = "Buddy is roled over"
        with unittest.mock.patch('builtins.print', side_effect=print) as mock_print:
            self.dog.roll_over()
            mock_print.assert_called_once_with(expected_output)

    def test_sit(self):
        expected_output = "Buddy is sitting"
        with unittest.mock.patch('builtins.print', side_effect=print) as mock_print:
            self.dog.sit()
            mock_print.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()
