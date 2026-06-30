from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Avg, Max, Min
import datetime
import json

from .models import DailyRecord
from .scoring import update_scores


# ==========================
# Dashboard
# ==========================

def dashboard(request):

    today = timezone.localdate()

    record = DailyRecord.objects.filter(date=today).first()

    context = {
        "record": record
    }

    return render(request, "analytics/dashboard.html", context)


# ==========================
# Today's Entry
# ==========================

def today(request):

    today_date = timezone.localdate()

    if request.method == "POST":

        record, created = DailyRecord.objects.update_or_create(

            date=today_date,

            defaults={

                # ---------------- Sleep ----------------

                "wake_time": request.POST.get("wake_time") or None,
                "bed_time": request.POST.get("bed_time") or None,
                "total_sleep": request.POST.get("total_sleep") or 0,

                # ---------------- Exercise ----------------

                "yoga": request.POST.get("yoga") or 0,
                "meditation": request.POST.get("meditation") or 0,
                "gym": request.POST.get("gym") or 0,
                "play": request.POST.get("play") or 0,

                # ---------------- Study ----------------

                "semester_study": request.POST.get("semester_study") or 0,
                "project": request.POST.get("project") or 0,
                "leetcode": request.POST.get("leetcode") or 0,
                "self_study": request.POST.get("self_study") or 0,

                # ---------------- Lifestyle ----------------

                "mobile": request.POST.get("mobile") or 0,
                "expense": request.POST.get("expense") or 0,

                # ---------------- Health ----------------

                "water": request.POST.get("water") or 0,
                "oil": request.POST.get("oil") or 0,
                "bath": request.POST.get("bath") or 0,
                "kayakalpam": request.POST.get("kayakalpam") or 0,

                # ---------------- Nutrition ----------------

                "protein": "protein" in request.POST,
                "milk": "milk" in request.POST,
                "fruits": "fruits" in request.POST,
                "amla_juice": "amla_juice" in request.POST,
                "sabja_badam": "sabja_badam" in request.POST,

                "maida": "maida" in request.POST,
                "white_sugar": "white_sugar" in request.POST,

                # ---------------- Learning ----------------

                "career_video": request.POST.get("career_video") or 0,
                "health_video": request.POST.get("health_video") or 0,
                "newspaper": request.POST.get("newspaper") or 0,
                "typewriting": request.POST.get("typewriting") or 0,
            }

        )

        # Reload from DB so all fields are proper Python types (not raw POST strings)
        record.refresh_from_db()

        # Calculate and save all scores
        update_scores(record)

        return redirect("dashboard")

    record = DailyRecord.objects.filter(date=today_date).first()

    context = {
        "record": record
    }

    return render(request, "analytics/today.html", context)


# ==========================
# Analytics
# ==========================

def analytics(request):

    records     = DailyRecord.objects.all().order_by("date")
    records_list = list(records)
    total        = len(records_list)

    # ---- Summary stats ----
    agg = records.aggregate(
        avg=Avg("overall_score"),
        best=Max("overall_score"),
        worst=Min("overall_score"),
    )
    avg_score   = round(agg["avg"]   or 0, 1)
    best_score  = round(agg["best"]  or 0, 1)
    worst_score = round(agg["worst"] or 0, 1)

    # ---- Chart data ----
    dates        = [r.date.strftime("%d %b") for r in records_list]
    overall_data = [r.overall_score           for r in records_list]
    study_data   = [r.study_score             for r in records_list]
    sleep_data   = [r.sleep_score             for r in records_list]
    water_data   = [float(r.water)            for r in records_list]
    mobile_data  = [float(r.mobile)           for r in records_list]

    # ---- Helper: time field → decimal hours ----
    def _tdec(t):
        return (t.hour + t.minute / 60) if t else None

    def _dec_to_str(v):
        h = int(v)
        m = round((v - h) * 60)
        return f"{h:02d}:{m:02d}"

    # ---- Per-parameter stats builder ----
    def pstat(label, field, best="max", unit="", is_time=False):
        if is_time:
            pairs = [(_tdec(getattr(r, field)), r.date)
                     for r in records_list if getattr(r, field) is not None]
            if not pairs:
                return {"label": label, "avg": "--", "best_val": "--", "best_date": "--", "unit": unit}
            avg_v = sum(v for v, _ in pairs) / len(pairs)
            fn = min if best == "min" else max
            bv, bd = fn(pairs, key=lambda x: x[0])
            return {"label": label, "avg": _dec_to_str(avg_v),
                    "best_val": _dec_to_str(bv), "best_date": bd, "unit": unit}
        else:
            pairs = [(float(getattr(r, field) or 0), r.date) for r in records_list]
            if not pairs:
                return {"label": label, "avg": "--", "best_val": "--", "best_date": "--", "unit": unit}
            avg_v = round(sum(v for v, _ in pairs) / len(pairs), 2)
            fn = min if best == "min" else max
            bv, bd = fn(pairs, key=lambda x: x[0])
            return {"label": label, "avg": avg_v, "best_val": bv, "best_date": bd, "unit": unit}

    param_stats = [
        # Sleep
        pstat("Wake Time",      "wake_time",      best="min", unit="",    is_time=True),
        pstat("Bed Time",       "bed_time",        best="min", unit="",    is_time=True),
        pstat("Total Sleep",    "total_sleep",     best="max", unit="hrs"),
        # Exercise
        pstat("Yoga",           "yoga",            best="max", unit="min"),
        pstat("Meditation",     "meditation",      best="max", unit="min"),
        pstat("Gym",            "gym",             best="max", unit="min"),
        pstat("Play",           "play",            best="max", unit="min"),
        # Study
        pstat("Semester Study", "semester_study",  best="max", unit="hrs"),
        pstat("Project",        "project",         best="max", unit="hrs"),
        pstat("LeetCode",       "leetcode",        best="max", unit="hrs"),
        pstat("Self Study",     "self_study",      best="max", unit="hrs"),
        # Health
        pstat("Water",          "water",           best="max", unit="L"),
        pstat("Oil (Head)",     "oil",             best="max", unit=""),
        pstat("Bath",           "bath",            best="max", unit=""),
        pstat("Kayakalpam",     "kayakalpam",      best="max", unit=""),
        # Lifestyle
        pstat("Mobile",         "mobile",          best="min", unit="hrs"),
        pstat("Career Video",   "career_video",    best="max", unit="min"),
        pstat("Health Video",   "health_video",    best="max", unit="min"),
        pstat("Newspaper",      "newspaper",       best="max", unit="min"),
        pstat("Typewriting",    "typewriting",     best="max", unit="min"),
        pstat("Expense",        "expense",         best="min", unit="₹"),
    ]

    # ---- Nutrition (boolean) stats ----
    bool_stats = []
    for label, field in [
        ("Protein",     "protein"),
        ("Milk",        "milk"),
        ("Fruits",      "fruits"),
        ("Amla Juice",  "amla_juice"),
        ("Sabja+Badam", "sabja_badam"),
        ("Maida",       "maida"),
        ("White Sugar", "white_sugar"),
    ]:
        count = sum(1 for r in records_list if getattr(r, field))
        pct   = round((count / total) * 100, 1) if total else 0
        bool_stats.append({"label": label, "count": count, "pct": pct})

    return render(
        request,
        "analytics/analytics.html",
        {
            "records":       records_list,
            "total":         total,
            "avg_score":     avg_score,
            "best_score":    best_score,
            "worst_score":   worst_score,
            "dates_json":    json.dumps(dates),
            "overall_json":  json.dumps(overall_data),
            "study_json":    json.dumps(study_data),
            "sleep_json":    json.dumps(sleep_data),
            "water_json":    json.dumps(water_data),
            "mobile_json":   json.dumps(mobile_data),
            "param_stats":   param_stats,
            "bool_stats":    bool_stats,
        }
    )


# ==========================
# History
# ==========================

def history(request):

    records = DailyRecord.objects.all().order_by("-date")

    avg_score = 0
    best_day  = None
    streak    = 0

    if records.exists():

        scores    = [r.overall_score for r in records]
        avg_score = round(sum(scores) / len(scores), 1)
        best_day  = max(records, key=lambda r: r.overall_score)

        # Current streak — consecutive days from today backwards
        today = timezone.localdate()
        for i, r in enumerate(records):
            if r.date == today - datetime.timedelta(days=i):
                streak += 1
            else:
                break

    return render(
        request,
        "analytics/history.html",
        {
            "records":   records,
            "avg_score": avg_score,
            "best_day":  best_day,
            "streak":    streak,
        }
    )


# ==========================
# Settings
# ==========================

def settings(request):

    return render(request, "analytics/settings.html")