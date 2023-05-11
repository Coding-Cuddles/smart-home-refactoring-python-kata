# Smart Home Refactoring Python Kata

[![CI](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml)
[![Replit](https://replit.com/badge?caption=Try%20with%20Replit&variant=small)](https://replit.com/new/github/Coding-Cuddles/smart-home-refactoring-python-kata)

## Overview

This kata complements [Clean Code: SOLID, Ep. 13 - Dependency Inversion Principle](https://cleancoders.com/episode/clean-code-episode-13).

## Instructions

In this kata, the `SmartHomeController` class directly depends on each concrete
class. This code violates the Dependency Inversion Principle because the
high-level `SmartHomeController` class should depend on abstractions, not on
low-level concrete classes. In the tests, we also directly manipulate the
`dimmable_light` and `networkable_light` instances to check their unique
behaviors.

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
