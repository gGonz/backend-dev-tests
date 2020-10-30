# 03 Pokémon catch test

Write a class named Pokemon that lets you define a name and a catch rate for a Pokémon.

The catch rate is a floating number between 0 and 1 that represents the base probability of a Pokémon to be caught when throwing a Poké Ball at it.

During battle, the Pokémon can be affected by a status condition that changes the probability of being caught.

The Pokemon class must define the following methods:

* `set_status(status)`: That lets you set a status condition on the Pokémon

* `catch_attempt(pokeball)`: That returns a boolean telling whether the Pokémon is caught or not, depending on the type of Poké Ball used, the status condition the Pokémon has (if any), and the catch rate of the Pokémon, by applying the following rules:

    1. If a `MASTER_BALL` is used, the Pokémon is caught.

    2. Generate a random number, N, depending on the type of Poké Ball used:
        * For a `POKE_BALL`: 0 to 255
        * For a `GREAT_BALL`: 0 to 200
        * For an `ULTRA_BALL`: 0 to 150

    3. The Pokémon is caught if:
        * It is in status `ASLEEP` or `FROZEN` and N is less than 25
        * It is in status `PARALYZED`, `BURNED` or `POISONED` and N is less than 12

    4. Otherwise, calculate the modified catch rate by dividing 25 by N and adding the result to the Pokémon's base catch rate. Use the modified catch rate as the  probability of the Pokémon to be caught.

Write your own unit tests in the provided TestCase for all the possible cases when trying to catch a Pokémon named "Pikachu" that has a catch rate of 35%.

You are only allowed to use `random` and no other library. In tests, you're allowed to use `mock` if needed.


## Instructions

1. Install the requirements with `pip install -r requirements.txt`
2. Run your tests with `coverage run -m unittest discover`
3. Check the coverage report with `coverage report -m`
4. Commit your work when the coverage report is 100%
