# Generated by Django 4.1.7 on 2023-04-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebSite', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not available', max_length=40),
        ),
    ]
