# Generated by Django 3.2.6 on 2023-03-06 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtesting', '0009_auto_20230306_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningoutcome',
            old_name='skill',
            new_name='skills',
        ),
    ]
