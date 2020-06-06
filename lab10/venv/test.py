import calculation
import unittest

class TestAdd(unittest.TestCase):
    """Test add funcion from file calculation"""
    def test_add_more_zero(self):
        """Test that the addition of two values more than 0, returns the correct total"""
        result = calculation.add(4,5)
        self.assertEqual(result,9)
    def test_add_less_zero(self):
        """Test that the addition of two values less than 0, returns the correct total"""
        result = calculation.add(-2,-4)
        self.assertEqual(result,-6)
    def test_add_with_zero(self):
        """Test that the addition of value with 0, returns the correct total"""
        result = calculation.add(5,0)
        self.assertEqual(result,5)

class TestSubtrac(unittest.TestCase):
    """Test subtract funcion from file calculation"""
    def test_subtract_more_zero(self):
        """Test that the subtract of two values more than 0, returns the correct total"""
        result = calculation.subtract(10,5)
        self.assertEqual(result,5)
    def test_subtract_less_zero(self):
        """Test that the subtract of two values less than 0, returns the correct total"""
        result = calculation.subtract(-5,-6)
        self.assertEqual(result,1)
    def test_subtract_with_zero(self):
        """Test that the subtract of value with 0, returns the correct total"""
        result = calculation.subtract(5,0)
        self.assertEqual(result,5)

def my_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add_with_zero"))
    suite.addTest(TestAdd("test_add_more_zero"))
    suite.addTest(TestSubtrac("test_subtract_with_zero"))
    suite.addTest(TestSubtrac("test_subtract_more_zero"))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

    '''result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtrac))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))'''

if __name__ == '__main__':
    my_suite()
    unittest.main()


