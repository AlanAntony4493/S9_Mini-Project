# Generated by Django 4.2.4 on 2023-09-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_prayergroup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_event',
            field=models.CharField(default='event selector', max_length=100),
        ),
    ]