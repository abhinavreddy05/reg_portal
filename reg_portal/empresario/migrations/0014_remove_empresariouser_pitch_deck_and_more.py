# Generated by Django 4.2.2 on 2023-07-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresario", "0013_empresariouser_pitch_deck_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="empresariouser",
            name="pitch_deck",
        ),
        migrations.AlterField(
            model_name="empresarioquestionnaire",
            name="pitch_deck",
            field=models.FileField(
                blank=True, null=True, upload_to="empresario/pitchdeck/"
            ),
        ),
    ]