# Generated by Django 4.2.2 on 2023-07-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresario", "0004_empresariouser_questionare_submitted"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresariouser",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]