# Generated by Django 4.2.4 on 2023-09-20 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_donor_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
