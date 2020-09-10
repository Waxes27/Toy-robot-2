import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot

class Test_robot(unittest.TestCase):
    @patch("sys.stdin",StringIO("HALBERD\n"))
    def test_name_of_the_robot(self):
        with patch("sys.stdout", new=StringIO()) as out:
            name = robot.name_of_the_robot()
            print(name)
            self.assertEqual(name,"HALBERD")
        #print(out.getvalue())

    @patch("sys.stdin", StringIO("HALBERD\n"))
    def test_get_command_input(self):
        with patch("sys.stdout", new=StringIO()) as out:
            name = robot.name_of_the_robot()

            output = out.getvalue() + name
            self.assertEqual(output,"What do you want to name your robot? HALBERD")
        print(output)
    
    def test_





if __name__ == '__main__':
    unittest.main()


