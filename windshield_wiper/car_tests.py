import unittest

from xmlrunner import xmlrunner

from windshield_wiper.models import Car


class CarTestCases(unittest.TestCase):
    def test_car(self):
        my_car = Car("AwesomeCars", "Model X")
        self.assertEqual(my_car.make, "AwesomeCars")
        self.assertEqual(my_car.model, "Model X")
        self.assertEqual(my_car.wiper.wear_level, 0)


if __name__ == '__main__':
    with open('results.xml', 'w') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=True,
            buffer=False,
            catchbreak=False
        )
