# Generated by Django 4.2.4 on 2023-09-24 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_answer_report_comment_answer_report_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='report_comment',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='report_count',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='reported_by',
        ),
    ]
