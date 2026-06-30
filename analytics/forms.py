from django import forms
from .models import DailyRecord


class DailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        exclude = [
            "daily_score",
            "created_at",
            "updated_at",
        ]