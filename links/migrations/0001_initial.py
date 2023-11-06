# Generated by Django 4.2.1 on 2023-08-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Friend",
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
                ("friend_name", models.CharField(max_length=50)),
                ("brief_introduction", models.CharField(max_length=100)),
                ("blog_url", models.URLField()),
                ("blog_avatar_url", models.URLField()),
            ],
        ),
    ]