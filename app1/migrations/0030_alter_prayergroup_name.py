# Generated by Django 4.2.4 on 2023-09-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_prayergroup_unique_case_sensitive_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayergroup',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]