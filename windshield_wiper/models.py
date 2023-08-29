class WindshieldWiper:
    def __init__(self, initial_wear=0):
        self.wear_level = initial_wear


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.wiper = WindshieldWiper()

    def activate_wipers(self, weather_condition):
        return self.wiper.wear_level < 90

    def handle_bird_strike(self):
        return self.wiper.wear_level < 80

    def check_wiper_fluid_level(self):
        return 50  # A random value, indicating wiper fluid is present
