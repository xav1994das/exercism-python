"""Functions used in preparing Guido's gorgeous lasagna."""

# 1. Define your constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    This function takes the number of layers you want to add to the lasagna
    and calculates the total preparation time using the PREPARATION_TIME constant.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time elapsed (prep + baking).

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking.
    :return: int - total number of minutes you've been cooking.

    This function sums the preparation time and the time the lasagna has already
    spent in the oven to find the total elapsed cooking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time