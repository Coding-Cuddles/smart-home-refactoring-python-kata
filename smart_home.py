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

    def dim(self, level):
        return f"Dimmable light dimmed to {level}%"


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


class SmartHomeController:

    def __init__(self):
        self.switchable_light = SwitchableLight()
        self.networkable_light = NetworkableLight()
        self.dimmable_light = DimmableLight()
        self.ac = AirConditioner()

    def turn_on_all(self):
        return [
            self.switchable_light.turn_on(),
            self.networkable_light.turn_on(),
            self.dimmable_light.turn_on(),
            self.ac.turn_on()
        ]

    def turn_off_all(self):
        return [
            self.switchable_light.turn_off(),
            self.networkable_light.turn_off(),
            self.dimmable_light.turn_off(),
            self.ac.turn_off()
        ]
