# Smart home refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Refactor the smart-home controller toward the Dependency Inversion Principle without changing its
behavior. Setup is complete when all four tests pass.

## Overview

This kata complements [Clean Code: SOLID, Ep. 13 - Dependency Inversion Principle](https://cleancoders.com/episode/clean-code-episode-13).

In this exercise, you'll practice refactoring code to adhere to the Dependency
Inversion Principle (DIP). You'll be working with a smart home system that
controls different types of lights and air conditioner.

## Instructions

### Exercise 1

The initial code consists of several device classes and the
`SmartHomeController` class, which is responsible for controlling all the
devices (lights and air conditioner).

However, the initial code violates the Dependency Inversion Principle, as the
`SmartHomeController` class directly depends on concrete classes. In the tests,
we also directly manipulate the `dimmable_light` and `networkable_light`
instances to check their unique behaviors.

Your goal is to refactor the code to adhere to the Dependency Inversion
Principle and make it easier to implement new devices.

Here are some guidelines to follow:

1. Introduce an interface or several interfaces (or abstract base classes) for
   the devices that the `SmartHomeController` interacts with.

1. Update the `SmartHomeController` class to depend on this interface, instead
   of the concrete device classes.

1. Update the devices to implement these interfaces.

1. Modify any constructors or method calls as necessary to accommodate the
   refactoring.

> [!NOTE]
>
> Remember that in this exercise, we assume all devices are in an ideal state
> and don't account for error cases such as a network connection failure or an
> attempt to dim a light below 0% or above 100% brightness.

Make sure the program still behaves the same way after your refactoring.
There's a unit test in place that checks that on a very rudimentary level by
just looking at the output of the program.

### Exercise 2

When you're done with refactoring, test the quality of your refactoring by
implementing two additional scenarios (methods) in `SmartHomeController`:

1. Add the `make_quick_breakfast` scenario to open the blinds and make a
   predefined coffee type.
   1. Add `Blinds` device class with `open` and `close` methods
      (blinds are always powered and does not have an on/off function).
   1. Add `make_quick_breakfast` method to `SmartHomeController`.

1. Add automatic vacuum cleaner and the `schedule_night_cleaning` scenario, which
   should start the cleaning once everything else is turned off.
   1. Add `VacuumCleaner` device class with `start_cleaning` and `stop_cleaning`
      methods.
   1. Add `schedule_night_cleaning` method to `SmartHomeController`. After
      calling this method, the vacuum cleaner should start cleaning once all
      other devices are turned off.

Evaluate whether your refactoring made life easier for you or not.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/smart-home-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd smart-home-refactoring-python-kata
   ```

3. Run the tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `4 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Refactor `SmartHomeController` and its devices in `smart_home.py` without changing their
   observable behavior.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   Continue when the test run completes without failures.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the available Make targets         |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
