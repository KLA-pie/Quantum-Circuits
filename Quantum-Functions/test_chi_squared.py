"""
Check the correctness of the chi-squared calculator
"""

import math
import pytest

from chi_squared_calc import chi_squared

CHI_SQUARED_COMPARISON = [
    ([1, 1, 1, 1], [1, 1, 1, 1], 0, "The results are not statisically significant"),
    (
        [0, 0, 0, 4],
        [1, 1, 1, 1],
        299996.25,
        "The results are statisically significant",
    ),
    ([1, 1, 1, 1], [0, 0, 0, 4], 12, "The results are statisically significant"),
    (
        [1, 12, 3, 4],
        [2, 7, 6, 5],
        6.333,
        "The results are not statisically significant",
    ),
    (
        [5, 5, 5, 5],
        [4, 6, 7, 3],
        2.0,
        "The results are not statisically significant",
    ),
    (
        [25, 25, 20, 15],
        [24, 24, 30, 7],
        9.347,
        "The results are statisically significant",
    ),
    (
        [36, 11, 32, 1],
        [27, 12, 29, 12],
        123.622,
        "The results are statisically significant",
    ),
    ([1, 1, 1, 1], [1, 1, 1, 1], 0, "The results are not statisically significant"),
    ([1, 1, 1, 1], [1, 1, 1, 1], 0, "The results are not statisically significant"),
    ([1, 1, 1, 1], [1, 1, 1, 1], 0, "The results are not statisically significant"),
    ([1, 1, 1, 1], [1, 1, 1, 1], 0, "The results are not statisically significant"),
]


@pytest.mark.parametrize(
    "theory_val, experimental_val, chi_val, sig_statement", CHI_SQUARED_COMPARISON
)
def test_chi_squared(theory_val, experimental_val, chi_val, sig_statement):
    """
    Test that an implementation for chi-squared correctly calculates the
    chi-squared value and a statement about the significance of the
    table is correct.

    Args:
        theory_val: The list of occurences a specific qubit configuration is expected to occur
        experimental_val: The list of occurences a specific qubit configuration actually occurs
        chi_val: The actual chi-squared value between the two lists
        sig_statement: The actual statement of whether or not the data is statistically significant
    """
    test_chi_val, test_sig_statement = chi_squared(theory_val, experimental_val)
    assert math.isclose(test_chi_val, chi_val)
    assert test_sig_statement == sig_statement


SIGNIFICANCE_COMPARISON = [
    (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        0.05,
        0,
        "The results are not statisically significant",
    ),
    (
        [0, 0, 0, 4],
        [1, 1, 1, 1],
        0.05,
        299996.25,
        "The results are statisically significant",
    ),
    ([1, 1, 1, 1], [0, 0, 0, 4], 0.05, 12, "The results are statisically significant"),
    (
        [1, 12, 3, 4],
        [2, 7, 6, 5],
        0.05,
        6.333,
        "The results are not statisically significant",
    ),
    (
        [5, 5, 5, 5],
        [4, 6, 7, 3],
        0.05,
        2.0,
        "The results are not statisically significant",
    ),
    (
        [25, 25, 20, 15],
        [24, 24, 30, 7],
        0.05,
        9.347,
        "The results are statisically significant",
    ),
    (
        [36, 11, 32, 1],
        [27, 12, 29, 12],
        0.05,
        123.622,
        "The results are statisically significant",
    ),
    (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        0.05,
        0,
        "The results are not statisically significant",
    ),
    (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        0.05,
        0,
        "The results are not statisically significant",
    ),
    (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        0.05,
        0,
        "The results are not statisically significant",
    ),
    (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        0.05,
        0,
        "The results are not statisically significant",
    ),
]


@pytest.mark.parametrize(
    "theory_val, experimental_val, sig_val, chi_val, sig_statement",
    SIGNIFICANCE_COMPARISON,
)
def test_significance(theory_val, experimental_val, sig_val, chi_val, sig_statement):
    """
    Test that an implementation for chi-squared correctly calculates the
    chi-squared value and a statement about the significance given by the
    input of the user

    Args:
        theory_val: The list of occurences a specific qubit configuration is expected to occur
        experimental_val: The list of occurences a specific qubit configuration actually occurs
        sig_val: The level of significance to statisitcally set the data (0.05 by default)
        chi_val: The actual chi-squared value between the two lists
        sig_statement: The actual statement of whether or not the data is statistically significant
    """
    test_chi_val, test_sig_statement = chi_squared(
        theory_val, experimental_val, sig_val
    )
    assert math.isclose(test_chi_val, chi_val)
    assert test_sig_statement == sig_statement
