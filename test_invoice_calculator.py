import unittest

from invoice_calculator import divide_pay

test_project_amount = 360.0
test_project_hours = {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}
test_expected_pay = {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0}

class InvoiceCalculatorTests(unittest.TestCase):

    # Does the divide_pay function as expected?
    
    def testDividedFairly(self):
        f = divide_pay(test_project_amount, test_project_hours)
        self.assertEqual(f, test_expected_pay)

    # Does the divide_pay function work if one of the people has zero hours?

    def testZeroHourPerson(self):
        pay = divide_pay(360.0, {"Alice":3.0, "Bob":6.0, "Carol":0.0})
        self.assertEqual(pay, {"Alice":120.0, "Bob":240.0, "Carol":0.0})

    # What if total hours is 0? Should be ValueError.

    def testZeroHoursTotal(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0} )

    # What if no people? Should be ValueError as total_hours is 0.
            
    def testNoPeople(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {})


    # Other test to look for edge cases:



            
if __name__ == "__main__":
    unittest.main()