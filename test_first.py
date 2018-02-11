import unittest
import xmlrunner


class TestCalc(unittest.TestCase):

    def test_dave(self):
        self.assertEqual(1,2)


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="python_unittests_xml"))