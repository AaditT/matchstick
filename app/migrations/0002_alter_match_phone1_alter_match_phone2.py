# Generated by Django 4.2.7 on 2023-12-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="phone1",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="match",
            name="phone2",
            field=models.IntegerField(),
        ),
    ]