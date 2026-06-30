from django.db import models


class DailyRecord(models.Model):
    # =========================
    # Date
    # =========================
    date = models.DateField(unique=True)

    # =========================
    # Sleep
    # =========================
    wake_time = models.TimeField(null=True, blank=True)
    bed_time = models.TimeField(null=True, blank=True)
    total_sleep = models.FloatField(default=0)

    # =========================
    # Exercise (minutes)
    # =========================
    yoga = models.PositiveIntegerField(default=0)
    meditation = models.PositiveIntegerField(default=0)
    gym = models.PositiveIntegerField(default=0)
    play = models.PositiveIntegerField(default=0)

    # =========================
    # Study (hours)
    # =========================
    semester_study = models.FloatField(default=0)
    project = models.FloatField(default=0)
    leetcode = models.FloatField(default=0)
    self_study = models.FloatField(default=0)

    # =========================
    # Lifestyle
    # =========================
    mobile = models.FloatField(default=0)      # hours
    expense = models.FloatField(default=0)     # ₹

    # =========================
    # Health
    # =========================
    water = models.FloatField(default=0)       # litres
    oil = models.PositiveIntegerField(default=0)
    bath = models.PositiveIntegerField(default=0)
    kayakalpam = models.PositiveIntegerField(default=0)

    # =========================
    # Nutrition
    # =========================
    protein = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    fruits = models.BooleanField(default=False)
    amla_juice = models.BooleanField(default=False)
    sabja_badam = models.BooleanField(default=False)

    maida = models.BooleanField(default=False)
    white_sugar = models.BooleanField(default=False)

    # =========================
    # Learning
    # =========================
    career_video = models.PositiveIntegerField(default=0)
    health_video = models.PositiveIntegerField(default=0)
    newspaper = models.PositiveIntegerField(default=0)
    typewriting = models.PositiveIntegerField(default=0)

    # =========================
    # Scores
    # =========================
    sleep_score = models.FloatField(default=0)
    exercise_score = models.FloatField(default=0)
    study_score = models.FloatField(default=0)
    nutrition_score = models.FloatField(default=0)
    health_score = models.FloatField(default=0)
    lifestyle_score = models.FloatField(default=0)

    overall_score = models.FloatField(default=0)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")