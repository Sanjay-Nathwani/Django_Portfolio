# Generated by Django 4.2.1 on 2023-05-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
