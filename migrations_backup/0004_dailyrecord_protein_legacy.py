from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0003_alter_dailyrecord_protein"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyrecord",
            name="protein",
            field=models.FloatField(default=0),
        ),
    ]