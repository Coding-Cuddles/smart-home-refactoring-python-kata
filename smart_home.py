class SwitchableLight:

    def turn_on(self):
        return "Switchable light turned on"

    def turn_off(self):
        return "Switchable light turned off"


class DimmableLight:

    def turn_on(self):
        return "Dimmable light turned on at full brightness"

    def turn_off(self):
        return "Dimmable light turned off"

    def dim(self, level_in_percent):
        return f"Dimmable light dimmed to {level_in_percent}%"


class NetworkableLight:

    def turn_on(self):
        return "Networkable light turned on"

    def turn_off(self):
        return "Networkable light turned off"

    def connect_to_network(self, network_name):
        return f"Networkable light connected to {network_name}"


class AirConditioner:

    def turn_on(self):
        return "AC turned on"

    def turn_off(self):
        return "AC turned off"

    def set_temperature(self, temperature_in_celsius):
        return f"Set temperature to {temperature_in_celsius}"


class CoffeeMaker:

    def turn_on(self):
        return "Coffee maker turned on"

    def turn_off(self):
        return "Coffee maker turned off"

    def brew(self, coffee_type):
        return f"Brewing {coffee_type} coffee"


class SmartHomeController:

    def __init__(self):
        self.switchable_light_1 = SwitchableLight()
        self.switchable_light_2 = SwitchableLight()
        self.networkable_light = NetworkableLight()
        self.dimmable_light = DimmableLight()
        self.coffee_maker = CoffeeMaker()
        self.ac = AirConditioner()

    def turn_on_all(self):
        return [
            self.switchable_light_1.turn_on(),
            self.switchable_light_2.turn_on(),
            self.networkable_light.turn_on(),
            self.dimmable_light.turn_on(),
            self.coffee_maker.turn_on(),
            self.ac.turn_on()
        ]

    def turn_off_all(self):
        return [
            self.switchable_light_1.turn_off(),
            self.switchable_light_2.turn_off(),
            self.networkable_light.turn_off(),
            self.dimmable_light.turn_off(),
            self.coffee_maker.turn_off(),
            self.ac.turn_off()
        ]
