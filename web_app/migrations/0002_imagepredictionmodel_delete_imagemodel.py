# Generated by Django 5.0.1 on 2024-02-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImagePredictionModel",
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
                ("image", models.ImageField(upload_to="uploaded_images/")),
                ("prediction", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="ImageModel",
        ),
    ]