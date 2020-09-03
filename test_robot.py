import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot

class Test_robot(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\n"))
    def test_get_command_input(self):
        sys.stdout = StringIO

        result = robot.robot_start()

        sys.stdout = sys.__stdout__

