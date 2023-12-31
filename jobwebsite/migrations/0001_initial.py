# Generated by Django 4.1.7 on 2023-04-01 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(default="", max_length=200)),
                ("company", models.CharField(default="", max_length=200)),
                ("salary", models.CharField(default="", max_length=200)),
                ("location", models.CharField(default="", max_length=200)),
                ("url", models.CharField(default="", max_length=1000)),
                ("description", models.CharField(default="", max_length=5000)),
                ("fullDescription", models.CharField(default="", max_length=50000)),
                ("favorite", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
