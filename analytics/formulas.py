"""
=========================================
LifeOS Formula Engine
=========================================

This file contains only mathematical formulas.

Every function returns a score between 0 and 100.

No Django code.
No database code.
No weights.

=========================================
"""

import math


# =========================================
# Clamp
# =========================================

def clamp(score):
    """
    Ensures score stays between 0 and 100.
    """

    return max(0, min(100, score))


# =========================================
# Bell Curve
# =========================================

def bell(value, ideal, sigma):
    """
    Gaussian Bell Curve

    Parameters
    ----------
    value : float
    ideal : float
    sigma : float

    Returns
    -------
    Score between 0 and 100
    """

    score = 100 * math.exp(
        -((value - ideal) ** 2) / (2 * sigma ** 2)
    )

    return clamp(score)


# =========================================
# Arctangent
# =========================================

def arctan(value, a):
    """
    Increasing curve.

    Starts at 0.

    Never reaches 100.

    Smooth slope.
    """

    if value <= 0:
        return 0

    score = (2 / math.pi) * math.atan(value / a) * 100

    return clamp(score)


# =========================================
# Reverse Arctangent
# =========================================

def reverse_arctan(value, a):
    """
    Decreasing curve.

    Starts near 100.

    Approaches 0.
    """

    score = 100 - arctan(value, a)

    return clamp(score)


# =========================================
# Boolean
# =========================================

def boolean(value):
    """
    True -> 100
    False -> 0
    """

    return 100 if value else 0


# =========================================
# Reverse Boolean
# =========================================

def reverse_boolean(value):
    """
    True -> 0
    False -> 100
    """

    return 0 if value else 100


# =========================================
# Kayakalpam
# =========================================

def kayakalpam(value):
    """
    Ideal:
        7

    >7
        Dangerous

    Score = 0

    <=7

        Linear

    0 -> 0

    7 ->100
    """

    if value > 7:
        return 0

    score = (value / 7) * 100

    return clamp(score)


# =========================================
# Average
# =========================================

def average(scores):
    """
    Average of scores.

    Ignores None.
    """

    valid = [
        s
        for s in scores
        if s is not None
    ]

    if len(valid) == 0:
        return 0

    return sum(valid) / len(valid)


# =========================================
# Weighted Average
# =========================================

def weighted_average(scores, weights):
    """
    Computes weighted average.
    """

    total_weight = sum(weights)

    if total_weight == 0:
        return 0

    weighted_sum = 0

    for s, w in zip(scores, weights):

        weighted_sum += s * w

    return weighted_sum / total_weight


# =========================================
# Percentage
# =========================================

def percentage(value, total):
    """
    Returns percentage.
    """

    if total == 0:
        return 0

    return (value / total) * 100


# =========================================
# Time to Decimal Hours
# =========================================

def time_to_hours(hour, minute):
    """
    Example

    4:45

    Returns

    4.75
    """

    return hour + minute / 60


# =========================================
# Decimal Hours to Time
# =========================================

def hours_to_time(value):
    """
    Example

    4.75

    Returns

    (4,45)
    """

    hour = int(value)

    minute = round((value - hour) * 60)

    return hour, minute