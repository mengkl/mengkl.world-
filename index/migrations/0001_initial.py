# Generated by Django 4.2.1 on 2023-08-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Myapps",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("my_apps_cn", models.CharField(blank=True, max_length=30)),
                ("my_apps_en", models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]