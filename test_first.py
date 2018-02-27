import unittest
import xmlrunner
from source import Test

class TestCalc(unittest.TestCase):

    def test_dave(self):
        self.assertEqual(1,1) 

    def test_adder(self):
        self.assertEqual(1,1)

    def test_sub1(self):
        self.assertEqual(3,3)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="python_unittests_xml"))