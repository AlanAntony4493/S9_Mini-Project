# Generated by Django 4.2.4 on 2024-02-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0051_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='executive_images/')),
            ],
        ),
    ]
