# Generated by Django 4.2.4 on 2023-10-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_careerresourceperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
