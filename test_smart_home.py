import pytest

from smart_home import SmartHomeController


@pytest.fixture
def controller():
    return SmartHomeController()


def test_turn_on_all(controller):
    assert controller.turn_on_all() == [
        "Switchable light turned on",
        "Switchable light turned on",
        "Networkable light turned on",
        "Dimmable light turned on at full brightness",
        "Coffee maker turned on",
        "AC turned on",
    ]


def test_turn_off_all(controller):
    assert controller.turn_off_all() == [
        "Switchable light turned off",
        "Switchable light turned off",
        "Networkable light turned off",
        "Dimmable light turned off",
        "Coffee maker turned off",
        "AC turned off",
    ]


def test_dim_light(controller):
    assert controller.dimmable_light.dim(50) == "Dimmable light dimmed to 50%"


def test_connect_light_to_network(controller):
    assert controller.networkable_light.connect_to_network(
        "Home Network") == "Networkable light connected to Home Network"
