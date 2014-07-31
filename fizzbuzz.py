import unittest
import xmlrunner


class FizzBuzzTest(unittest.TestCase):
    def test_number_divisible_by_3_return_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, "FIZZ")


class FizzBuzz:
    def take(self, number):
        return "FIZZ"

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
