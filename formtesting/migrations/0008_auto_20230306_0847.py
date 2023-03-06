# Generated by Django 3.2.6 on 2023-03-06 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formtesting', '0007_auto_20230304_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningoutcome',
            name='skill',
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formtesting.skill'),
        ),
    ]