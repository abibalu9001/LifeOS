"""
=========================================
LifeOS Scoring Engine
=========================================

This file calculates every score.

Uses:
    formulas.py
    constants.py

=========================================
"""

from datetime import time

from .formulas import (
    bell,
    arctan,
    reverse_arctan,
    boolean,
    reverse_boolean,
    kayakalpam,
    average,
    weighted_average
)

from .constants import *


# ==========================================
# Time Conversion
# ==========================================

def decimal_hour(t):

    """
    Converts datetime.time to decimal hours.

    Example

    4:45

    becomes

    4.75
    """

    if t is None:
        return 0

    return t.hour + t.minute / 60


# ==========================================
# Sleep Score
# ==========================================

def sleep_score(record):

    wake = bell(
        decimal_hour(record.wake_time),
        WAKE_TIME_IDEAL,
        WAKE_TIME_SIGMA
    )

    bed = bell(
        decimal_hour(record.bed_time),
        BED_TIME_IDEAL,
        BED_TIME_SIGMA
    )

    sleep = bell(
        record.total_sleep,
        TOTAL_SLEEP_IDEAL,
        TOTAL_SLEEP_SIGMA
    )

    score = weighted_average(

        [
            wake,
            bed,
            sleep
        ],

        [
            WEIGHTS["wake_time"],
            WEIGHTS["bed_time"],
            WEIGHTS["total_sleep"]
        ]

    )

    return round(score, 2)


# ==========================================
# Exercise Score
# ==========================================

def exercise_score(record):

    yoga = arctan(
        record.yoga,
        YOGA_A
    )

    meditation = arctan(
        record.meditation,
        MEDITATION_A
    )

    gym = arctan(
        record.gym,
        GYM_A
    )

    play = arctan(
        record.play,
        PLAY_A
    )

    score = weighted_average(

        [
            yoga,
            meditation,
            gym,
            play
        ],

        [
            WEIGHTS["yoga"],
            WEIGHTS["meditation"],
            WEIGHTS["gym"],
            WEIGHTS["play"]
        ]

    )

    return round(score,2)


# ==========================================
# Study Score
# ==========================================

def study_score(record):

    semester = arctan(
        record.semester_study,
        SEMESTER_STUDY_A
    )

    project = arctan(
        record.project,
        PROJECT_A
    )

    leetcode = arctan(
        record.leetcode,
        LEETCODE_A
    )

    selfstudy = arctan(
        record.self_study,
        SELF_STUDY_A
    )

    total_study = average(

        [
            semester,
            project,
            leetcode,
            selfstudy
        ]

    )

    score = weighted_average(

        [

            semester,

            project,

            leetcode,

            selfstudy,

            total_study

        ],

        [

            WEIGHTS["semester_study"],

            WEIGHTS["project"],

            WEIGHTS["leetcode"],

            WEIGHTS["self_study"],

            5

        ]

    )

    return round(score,2)

# ==========================================
# Nutrition Score
# ==========================================

def nutrition_score(record):

    protein = boolean(record.protein)

    milk = boolean(record.milk)

    fruits = boolean(record.fruits)

    amla = boolean(record.amla_juice)

    sabja = boolean(record.sabja_badam)

    maida = reverse_boolean(record.maida)

    sugar = reverse_boolean(record.white_sugar)

    score = weighted_average(

        [

            protein,

            milk,

            fruits,

            amla,

            sabja,

            maida,

            sugar

        ],

        [

            WEIGHTS["protein"],

            2,                     # Milk

            WEIGHTS["fruits"],

            WEIGHTS["amla_juice"],

            WEIGHTS["sabja_badam"],

            WEIGHTS["maida"],

            WEIGHTS["white_sugar"]

        ]

    )

    return round(score,2)


# ==========================================
# Health Score
# ==========================================

def health_score(record):

    water = arctan(

        record.water,

        WATER_A

    )

    oil = arctan(

        record.oil,

        OIL_A

    )

    bath = arctan(

        record.bath,

        BATH_A

    )

    kaya = kayakalpam(

        record.kayakalpam

    )

    score = weighted_average(

        [

            water,

            oil,

            bath,

            kaya

        ],

        [

            WEIGHTS["water"],

            WEIGHTS["oil"],

            WEIGHTS["bath"],

            WEIGHTS["kayakalpam"]

        ]

    )

    return round(score,2)


# ==========================================
# Lifestyle Score
# ==========================================

def lifestyle_score(record):

    mobile = reverse_arctan(

        record.mobile,

        MOBILE_A

    )

    career = arctan(

        record.career_video,

        CAREER_VIDEO_A

    )

    health = arctan(

        record.health_video,

        HEALTH_VIDEO_A

    )

    newspaper = arctan(

        record.newspaper,

        NEWSPAPER_A

    )

    typing = arctan(

        record.typewriting,

        TYPEWRITING_A

    )

    expense = reverse_arctan(

        record.expense,

        EXPENSE_A

    )

    score = weighted_average(

        [

            mobile,

            career,

            health,

            newspaper,

            typing,

            expense

        ],

        [

            WEIGHTS["mobile"],

            WEIGHTS["career_video"],

            WEIGHTS["health_video"],

            WEIGHTS["newspaper"],

            WEIGHTS["typewriting"],

            WEIGHTS["expense"]

        ]

    )

    return round(score,2)

# ==========================================
# Overall Score
# ==========================================

def overall_score(record):
    """
    Calculates the final LifeOS score.
    """

    sleep = sleep_score(record)

    exercise = exercise_score(record)

    study = study_score(record)

    nutrition = nutrition_score(record)

    health = health_score(record)

    lifestyle = lifestyle_score(record)

    score = weighted_average(

        [
            sleep,
            exercise,
            study,
            nutrition,
            health,
            lifestyle
        ],

        [
            5,      # Sleep
            5,      # Exercise
            5,      # Study
            4,      # Nutrition
            4,      # Health
            4       # Lifestyle
        ]

    )

    return round(score, 2)


# ==========================================
# Calculate All Scores
# ==========================================

def calculate_scores(record):
    """
    Calculates every score and stores them
    inside the model.
    """

    record.sleep_score = sleep_score(record)

    record.exercise_score = exercise_score(record)

    record.study_score = study_score(record)

    record.nutrition_score = nutrition_score(record)

    record.health_score = health_score(record)

    record.lifestyle_score = lifestyle_score(record)

    record.overall_score = overall_score(record)

    return record


# ==========================================
# Save Scores
# ==========================================

def update_scores(record):
    """
    Calculates and saves scores.
    """

    calculate_scores(record)

    record.save()

    return record