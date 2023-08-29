import unittest

import xmlrunner

from windshield_wiper.models import Car
from windshield_wiper.service import WindshieldWiperService


class IntegrationWindshieldWiperTestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car("AwesomeCars", "Model X")
        self.wiper_service = WindshieldWiperService()

    def test_wiper_wear_normal(self):
        wear_level = self.wiper_service.get_wiper_wear_level(self.car)
        self.assertLessEqual(wear_level, 50, "Wipers are surprisingly fashionable for something with a 'wear' level!")

    def test_wiper_wear_high(self):
        self.wiper_service.increase_wiper_wear(self.car, 90)
        wear_level = self.wiper_service.get_wiper_wear_level(self.car)
        self.assertGreaterEqual(wear_level, 90,
                                "Wipers have embraced their inner hipster and grown their wear level to 'vintage'.")

    def test_wiper_wear_replacement(self):
        self.wiper_service.increase_wiper_wear(self.car, 95)
        wear_level = self.wiper_service.get_wiper_wear_level(self.car)
        if wear_level >= 95:
            replacement_message = self.wiper_service.replace_wipers(self.car)
            self.assertIn("new wipers", replacement_message,
                          "Wipers are retiring to a beach resort. Time for some fresh talent!")

if __name__ == '__main__':
    with open('results.xml', 'w') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=True,
            buffer=False,
            catchbreak=False
        )

