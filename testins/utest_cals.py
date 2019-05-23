import unittest
import calc

class CalcTest(unittest.TestCase):
    """Calc tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print('setUpClass')
        print('==========')

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print('tearDownClass')
        print('==========')

    def setUp(self):
        """Set up for test"""
        print(f"Set up for [{self.shortDescription()}]")

    def TearDown(self):
        """Tear down for test"""
        print(f"Tear down for [{self.shortDescription()}]")

    def test_add(self):
        self.assertEqual(calc.add(1, 3), 4)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 2), 8)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 5), 15)

    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)


if __name__ == "__main__":
    unittest.main()


