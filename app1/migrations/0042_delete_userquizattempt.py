# Generated by Django 4.2.4 on 2023-09-29 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_quizcategory_quizquestion_userquizattempt_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserQuizAttempt',
        ),
    ]