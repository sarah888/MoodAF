# Generated by Django 4.0.6 on 2023-05-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='feedback',
            field=models.TextField(default='No feedback'),
        ),
    ]