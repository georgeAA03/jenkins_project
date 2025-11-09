import unittest
from app import greet

class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World from George Abou Assaleh"), "Hello, World from George Abou Assaleh!")

if __name__ == "__main__":
    unittest.main()