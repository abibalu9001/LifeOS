"""
=========================================
LifeOS Configuration
=========================================
Modify values here.
No other file should contain magic numbers.
"""

# =========================================
# IDEAL VALUES (Bell Curve)
# =========================================

# Wake Time (4:45 AM)
WAKE_TIME_IDEAL = 4.75
WAKE_TIME_SIGMA = 0.75

# Bed Time (9:00 PM)
BED_TIME_IDEAL = 21.0
BED_TIME_SIGMA = 0.75

# Total Sleep (hours)
TOTAL_SLEEP_IDEAL = 7.75
TOTAL_SLEEP_SIGMA = 1.0


# =========================================
# Arctangent "a" Values
# =========================================

YOGA_A = 20
MEDITATION_A = 10
GYM_A = 20
PLAY_A = 30

SEMESTER_STUDY_A = 4
PROJECT_A = 1
LEETCODE_A = 0.5
SELF_STUDY_A = 1

WATER_A = 3

OIL_A = 1
BATH_A = 2

CAREER_VIDEO_A = 1
HEALTH_VIDEO_A = 1

NEWSPAPER_A = 10
TYPEWRITING_A = 10


# =========================================
# Reverse Arctangent
# =========================================

MOBILE_A = 4
EXPENSE_A = 100


# =========================================
# Kayakalpam
# =========================================

KAYAKALPAM_IDEAL = 7
KAYAKALPAM_MAX = 7


# =========================================
# Parameter Weights
# =========================================

WEIGHTS = {

    # ---------- High ----------

    "wake_time": 5,
    "bed_time": 5,

    "yoga": 5,
    "meditation": 5,
    "gym": 5,
    "play": 5,

    "mobile": 5,

    "semester_study": 5,
    "project": 5,

    "protein": 5,

    "kayakalpam": 5,

    # ---------- Medium ----------

    "leetcode": 3,

    "water": 3,

    "oil": 3,

    "maida": 3,
    "white_sugar": 3,

    "fruits": 3,

    "career_video": 3,
    "health_video": 3,

    "self_study": 3,

    # ---------- Low ----------

    "total_sleep": 1,

    "amla_juice": 1,
    "sabja_badam": 1,

    "bath": 1,

    "newspaper": 1,
    "typewriting": 1,

    "expense": 1,

}


# =========================================
# Boolean Scores
# =========================================

TRUE_SCORE = 100
FALSE_SCORE = 0

REVERSE_TRUE_SCORE = 0
REVERSE_FALSE_SCORE = 100


# =========================================
# Score Limits
# =========================================

MIN_SCORE = 0
MAX_SCORE = 100


# =========================================
# Graph Colors
# =========================================

PRIMARY = "#2563EB"
SUCCESS = "#10B981"
WARNING = "#F59E0B"
DANGER = "#EF4444"
INFO = "#0EA5E9"
SECONDARY = "#64748B"


# =========================================
# Date Formats
# =========================================

DATE_FORMAT = "%d-%m-%Y"
TIME_FORMAT = "%H:%M"


# =========================================
# Dashboard
# =========================================

TOP_DAYS = 10
RECENT_DAYS = 7