from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Today's Entry
    path("today/", views.today, name="today"),

    # Analytics
    path("analytics/", views.analytics, name="analytics"),

    # History
    path("history/", views.history, name="history"),

    # Settings
    path("settings/", views.settings, name="settings"),

]