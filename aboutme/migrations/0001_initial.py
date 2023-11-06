# Generated by Django 4.2.1 on 2023-08-20 19:19

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutMe",
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
                ("title", models.CharField(max_length=50)),
                ("body", mdeditor.fields.MDTextField()),
                ("body_after_changed", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
