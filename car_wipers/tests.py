import unittest

import xmlrunner

from car_wipers.service import CarWipersService


class CarWipersTestCase(unittest.TestCase):
    def setUp(self):
        self.car_wipers = CarWipersService()

    def test_wipers_light_rain(self):
        self.assertTrue(self.car_wipers.activate_wipers("light rain"), "Wipers couldn't handle light rain!")

    def test_wipers_monsoon(self):
        self.assertTrue(self.car_wipers.activate_wipers("monsoon"), "Did the car just turn into a submarine?")

    def test_wipers_snowstorm(self):
        self.assertTrue(self.car_wipers.activate_wipers("snowstorm"), "Wipers are now painting abstract art with snow!")

    def test_wipers_desert(self):
        self.assertFalse(self.car_wipers.activate_wipers("sandstorm"), "Wipers are searching for water in the desert.")

    def test_bird_strike(self):
        self.assertTrue(self.car_wipers.handle_bird_strike(), "Wipers are having a feathered dance party!")

    def test_wiper_fluid_level(self):
        self.assertGreater(self.car_wipers.check_wiper_fluid_level(), 0, "Wiper fluid level is non-existent!")


if __name__ == '__main__':
    with open('results.xml', 'w') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False,
            buffer=False,
            catchbreak=False
        )
