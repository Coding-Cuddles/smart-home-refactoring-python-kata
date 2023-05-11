# Smart Home Refactoring Python Kata

[![CI](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml)
[![Replit](https://replit.com/badge?caption=Try%20with%20Replit&variant=small)](https://replit.com/new/github/Coding-Cuddles/smart-home-refactoring-python-kata)

## Overview

This kata complements [Clean Code: SOLID, Ep. 13 - Dependency Inversion Principle](https://cleancoders.com/episode/clean-code-episode-13).

In this exercise, you'll practice refactoring code to adhere to the Dependency
Inversion Principle (DIP). You'll be working with a smart home system that
controls different types of lights and an air conditioner.

## Instructions

The initial code consists of the following classes:

* `SwitchableLight`
* `DimmableLight`
* `NetworkableLight`
* `AirConditioner`
* `SmartHomeController`

The `SmartHomeController` class is responsible for controlling all the devices
(lights and air conditioner). However, the initial code violates the Dependency
Inversion Principle, as the `SmartHomeController` class directly depends on
concrete classes. In the tests, we also directly manipulate the
`dimmable_light` and `networkable_light` instances to check their unique
behaviors.

Your goal is to refactor the code to adhere to the Dependency Inversion
Principle. Here are some guidelines to follow:

1. Introduce an interface (or an abstract base class) for the devices that the
   `SmartHomeController` interacts with.
1. Update the `SmartHomeController` class to depend on this interface, instead
   of the concrete device classes.
1. Update the devices (`SwitchableLight`, `DimmableLight`, `NetworkableLight`,
   and `AirConditioner`) to implement this interface.
1. Modify any constructors or method calls as necessary to accommodate the
   refactoring.

> **Note**
>
> Remember that in this exercise, we assume all devices are in an ideal state
> and don't account for error cases such as a network connection failure or an
> attempt to dim a light below 0% or above 100% brightness.

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```
