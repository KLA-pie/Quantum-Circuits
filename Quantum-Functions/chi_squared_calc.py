"""
A Chi-squared calculator for comparing experimental
and theoretical values for Qubit configurations
"""


def chi_squared(theory_val, experimental_val):
    """
    Calculates the Chi-Squared value between the theoretical
    values for qubits and the experimental/real value for qubits

    Args:
        theory_val: A list of integers that represents the number of instances
        the IBM qubit configuration (00, 01, 10, 11) is expected occurs.

        experimental_val: A list of integers that represents the number of instances
        the IBM qubit configuration (00, 01, 10, 11) is actually occured in our randomly
        defined circuit.

    Returns:
        The Chi-squared value of the dataset
    """
    if len(theory_val) != len(experimental_val):
        return None, "List lengths must be the same"

    if abs(sum(theory_val) - sum(experimental_val)) > 0.001:
        return None, "List sums must be the same"

    # This calculates the chi-squared value of the given data point
    chi_value = 0
    for i in range(4):
        try:
            chi_value += (experimental_val[i] - theory_val[i]) ** 2 / theory_val[i]
        except ZeroDivisionError:
            chi_value += (experimental_val[i] - 0.00001) ** 2 / 0.00001
    return chi_value


def significance_statement(chi_value, significance=0.05):
    """
    Determines if the Chi squared value is statistically significant
    with a specified level of significance.

    Args:
        chi_value: A float that represents the Chi squared value calculated between the
        expected and observed values of qubit values.

        significance: A float between 0 and 1 (non-inclusive) that is meant to represent
        the level of significance the Chi-squared test may exceed for the experimental and
        theoretical data to be independent. The value is preset to 0.05
    Returns:
        A string explaining whether or not the data is statistically
        significant.
    """

    # Define a list of known chi-squared values respective to significance
    # values of 3 degrees of freedom
    significance_list = [0.115, 0.352, 0.584, 1.212, 2.366, 4.11, 6.25, 7.81, 11.34]
    significance_level = [0.99, 0.95, 0.90, 0.75, 0.50, 0.25, 0.10, 0.05, 0.01]
    lowest_significance = 1
    significance_index = 0
    invariant_boolean = False
    for i, sig_fig in enumerate(significance_level):
        approximate_significance = sig_fig - significance
        if abs(approximate_significance) < abs(lowest_significance):
            lowest_significance = approximate_significance
            significance_index = i

    # Iterate through the list to see if the significance is in the list
    for i, level_index in enumerate(significance_level):
        if abs(level_index - significance) < 0.001:
            invariant_boolean = True
            index = i
            break

    # Check to see if a given significant value is in the significant level list
    if invariant_boolean is True:
        relative_chi = significance_list[index]
    else:
        if lowest_significance < 0:
            relative_chi = (
                significance_list[significance_index]
                - significance_list[significance_index - 1]
            ) * lowest_significance + significance_list[i]
        else:
            relative_chi = (
                significance_list[significance_index + 1]
                - significance_list[significance_index]
            ) * lowest_significance + significance_list[i]

    # Determine if the data is statistically significant
    if relative_chi > chi_value:
        significance_string = "The results are not statisically significant"
    else:
        significance_string = "The results are statisically significant"

    return round(chi_value, 3), significance_string
