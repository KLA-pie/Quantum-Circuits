"""
Check the correctness of the chi-squared calculator
"""

import math
import pytest

from chi_squared_calc import chi_squared, significance_statement

CHI_SQUARED_COMPARISON = [
    # Test that a trivial case outputs zero
    ([1, 1, 1, 1], [1, 1, 1, 1], 0),
    # Test a case where the expected values are zero
    (
        [0, 0, 0, 4],
        [1, 1, 1, 1],
        299996.25,
    ),
    # Test a case where the observed values are zero
    ([1, 1, 1, 1], [0, 0, 0, 4], 12),
    # Test a case where the observed and expected values are varied
    (
        [1, 12, 3, 4],
        [2, 7, 6, 5],
        6.333,
    ),
    # Test a case where the observed and expected values are uniform
    (
        [5, 5, 5, 5],
        [4, 6, 7, 3],
        2.0,
    ),
    # Test a case where two values are noticeably different in the observed
    # and expected values
    (
        [25, 25, 20, 15],
        [24, 24, 30, 7],
        9.347,
    ),
    # Test a case where the 00 and 11 configurations are noticeably extreme
    (
        [36, 11, 32, 1],
        [27, 12, 29, 12],
        123.622,
    ),
    # Test a case where only one configiruation is extreme
    (
        [68, 71, 2, 5],
        [67, 68, 1, 10],
        5.641,
    ),
    # Test a case for uniform measured values
    (
        [257, 257, 255, 255],
        [256, 256, 256, 256],
        0.016,
    ),
    # Test a case for uniform expected values
    (
        [256, 256, 256, 256],
        [257, 257, 255, 255],
        0.016,
    ),
    # Test a case of egregious values for all configurations
    (
        [1000, 1001, 2000, 1],
        [900, 1, 3100, 1],
        1614.001,
    ),
]


@pytest.mark.parametrize(
    "theory_val, experimental_val, chi_val", CHI_SQUARED_COMPARISON
)
def test_chi_squared(theory_val, experimental_val, chi_val):
    """
    Test that an implementation for chi-squared correctly calculates the
    chi-squared value and a statement about the significance of the
    table is correct.

    Args:
        theory_val: The list of occurences a specific qubit configuration is expected to occur
        experimental_val: The list of occurences a specific qubit configuration actually occurs
        chi_val: The actual chi-squared value between the two lists
    """
    test_chi_val = chi_squared(theory_val, experimental_val)
    assert math.isclose(test_chi_val, chi_val)
    # assert test_sig_statement == sig_statement


SIGNIFICANCE_COMPARISON = [
    # Test a case with zero significance with a high significance value
    (0, 0.99, "The results are not statisically significant"),
    # Test a case with zero significance with a moderate significance value
    (0, 0.15, "The results are not statisically significant"),
    # Test a case with zero significance with a low significance value
    (0, 0.05, "The results are not statisically significant"),
    # Test a case with zero significance with a very low significance value
    (0, 0.01, "The results are not statisically significant"),
    # Test a case with high significance with a low significance value
    (12, 0.05, "The results are statisically significant"),
    # Test a case with high significance with a very low significance value
    (12, 0.01, "The results are statisically significant"),
    # Test a case with medium significance with a medium significance value
    (6.333, 0.25, "The results are statisically significant"),
    # Test a case with medium significance with a moderately low significance value
    (6.333, 0.10, "The results are statisically significant"),
    # Test a case with medium significance with a low significance value
    (6.333, 0.05, "The results are not statisically significant"),
    # Test a case with medium significance with a very low significance value
    (6.333, 0.01, "The results are not statisically significant"),
    # Test a case with low significance with a moderately low significance value
    (2.0, 0.05, "The results are not statisically significant"),
    # Test a case with a moderately high significance with a low significance value
    (9.347, 0.05, "The results are statisically significant"),
    # Test a case with a moderately high significance with a high significance value
    (9.347, 0.01, "The results are not statisically significant"),
    # Test a case with a very high significance with a low significance value
    (123.622, 0.05, "The results are statisically significant"),
    # Test a case with a very low significance with a high significance value
    (0.016, 0.05, "The results are not statisically significant"),
    # Test a case with an egregiously high significance with
    # a low significance value
    (1614.001, 0.05, "The results are statisically significant"),
    # Test a case with an egregiously high significance with
    # a very low significance value between two knowns closer to
    # the upper bound
    (1614.001, 0.035372, "The results are statisically significant"),
    # Test a case with an egregiously high significance with
    # a very low significance value between two knowns closer to
    # the lower bound
    (1614.001, 0.02, "The results are statisically significant"),
    # Test a case with an egregiously high significance with
    # a very low significance value between two knowns
    (1614.001, 0.01, "The results are statisically significant"),
]


@pytest.mark.parametrize(
    "chi_val, sig_val, sig_statement",
    SIGNIFICANCE_COMPARISON,
)
def test_significance(chi_val, sig_val, sig_statement):
    """
    Test that an implementation for chi-squared correctly calculates the
    chi-squared value and a statement about the significance given by the
    input of the user

    Args:
        chi_val: The calcualted chi-squared value after comparing data
        sig_val: The level of significance to statisitcally set the data (0.05 by default)
        sig_statement: The actual statement of whether or not the data is statistically significant
    """
    test_sig_statement = significance_statement(chi_val, sig_val)
    assert test_sig_statement == sig_statement
