# Generated by Django 3.2.14 on 2022-07-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plants",
            name="location",
            field=models.TextField(default="none"),
            preserve_default=False,
        ),
    ]
