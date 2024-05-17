# Generated by Django 4.1.7 on 2023-04-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studid', models.IntegerField()),
                ('stuname', models.CharField(max_length=60)),
                ('stuemail', models.EmailField(max_length=60)),
                ('stupass', models.CharField(max_length=50)),
            ],
        ),
    ]
