from windshield_wiper.models import WindshieldWiper


class WindshieldWiperService:
    @staticmethod
    def activate_wipers(weather_condition):
        # Simulate wipers activating based on weather conditions
        if weather_condition in ["light rain", "monsoon", "snowstorm"]:
            return True
        return False

    @staticmethod
    def handle_bird_strike():
        # Simulate wipers activating frantically after a bird strike
        return True

    @staticmethod
    def check_wiper_fluid_level():
        # Simulate checking wiper fluid level
        return 50  # A random value, indicating wiper fluid is present

    @staticmethod
    def get_wiper_wear_level(car):
        return car.wiper.wear_level

    @staticmethod
    def increase_wiper_wear(car, param):
        car.wiper.wear_level = param

    @staticmethod
    def replace_wipers(car):
        car.wiper = WindshieldWiper()
        return f"new wipers"


# You can create an instance of CarWipersService and use it in your tests
if __name__ == '__main__':
    car_wipers = WindshieldWiperService()
