from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyrecord',
            name='total_sleep',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='extra_sleep',
            field=models.FloatField(default=0),
        ),
    ]
