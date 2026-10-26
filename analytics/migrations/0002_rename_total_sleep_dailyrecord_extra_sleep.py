from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dailyrecord",
            old_name="total_sleep",
            new_name="extra_sleep",
        ),
    ]