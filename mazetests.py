import unittest
from Maze import *


class testMaze(unittest.TestCase):
    def setUp(self):
        # this checks for a Maze class
        self.m=Maze()

    def testScreenExists(self):
        assert type(self.m) == Maze

if __name__=="__main__":
    unittest.main(exit=False)

from Maze import *
import random
import turtle
import unittest

class testMaze(unittest.TestCase):
    """
    This class inherits from a class called TestCase which is defined
    in the unittest module.

    When you inherit from a class, you get all the methods that are defined
    in the class for free.

    Since this is a TestCase class, calling unittest.main() will automatically
    run any of the functions that start with the word 'test'
    """

    def setUp(self):
        """
        The setUP function is called each time one of your tests is run.
        We create an instance of the maze here before each test.
        """

        self.m=Maze()

    def testMazeExists(self):
        """
        this will check to see if we have a maze class but as soon
        as setUp is run, we will see a failure so we really don't
        need to do anything here
        """

        pass

#   def testScreenExists(self):
#       assert type(self.m.s) == turtle._Screen

unittest.main()

