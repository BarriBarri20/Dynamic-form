# Generated by Django 3.2 on 2023-03-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formtesting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_description',
            field=models.CharField(blank=True, help_text='Session Description', max_length=2560, null=True),
        ),
    ]
