"""
A Chi-squared calculator for comparing experimental
and theoretical values for Qubit configurations
"""


def Chi_Squared(theory_val, experimental_val, significance=0.05):
    """
    Calculates the statistical significance between the theoretical
    values for qubits and the experimental/real value for qubits

    Args:
        theory_val: A list of integers that represents the number of instances
        the IBM qubit configuration (00, 01, 10, 11) is expected occurs.

        experimental_val: A list of integers that represents the number of instances
        the IBM qubit configuration (00, 01, 10, 11) is actually occured in our randomly
        defined circuit.

        significance: A float between 0 and 1 that is meant to represent the level of
        significance the Chi-squared test may exceed for the experimental and theoretical
        data to be independent. The value is preset to 0.05

    Returns:
        The Chi-squared value and whether or not the data is statistically significant
    """
    sum = 0
    for i in theory_val:
        sum += ((experimental_val[i] - theory_val[i]) ^ 2 / theory_val[i]) ^ 1 / 2
