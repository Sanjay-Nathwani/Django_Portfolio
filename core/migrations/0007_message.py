# Generated by Django 4.2.1 on 2023-05-22 19:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_project_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("name", models.CharField(max_length=250, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("subject", models.CharField(max_length=250, null=True)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
