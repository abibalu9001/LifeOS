from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_rename_total_sleep_dailyrecord_extra_sleep"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dailyrecord",
            old_name="protein",
            new_name="protein_legacy",
        ),
    ]