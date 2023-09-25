# Generated by Django 4.2.4 on 2023-09-24 04:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0033_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='report_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='report_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='reported_by',
            field=models.ManyToManyField(related_name='reported_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]
