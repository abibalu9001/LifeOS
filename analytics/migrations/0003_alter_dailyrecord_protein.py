from django.db import migrations, models


def convert_protein_to_numeric(apps, schema_editor):
    DailyRecord = apps.get_model("analytics", "DailyRecord")
    connection = schema_editor.connection

    if connection.vendor == "postgresql":
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE analytics_dailyrecord
                ALTER COLUMN protein TYPE double precision
                USING 0.0
            """)
    elif connection.vendor == "sqlite":
        # SQLite's existing local database already has a numeric
        # protein column. Do not perform a database alteration here.
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_rename_total_sleep_dailyrecord_extra_sleep"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(
                    convert_protein_to_numeric,
                    migrations.RunPython.noop,
                ),
            ],
            state_operations=[
                migrations.AlterField(
                    model_name="dailyrecord",
                    name="protein",
                    field=models.FloatField(default=0),
                ),
            ],
        ),
    ]