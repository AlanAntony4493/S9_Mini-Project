# Generated by Django 4.2.4 on 2023-09-17 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_parishdirectory_is_active_prayergroup_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parishdirectory',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='prayergroup',
            name='is_active',
        ),
    ]
