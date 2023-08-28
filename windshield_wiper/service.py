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


# You can create an instance of CarWipersService and use it in your tests
if __name__ == '__main__':
    car_wipers = WindshieldWiperService()
