# Generated by Django 5.0.1 on 2024-01-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0003_alter_coinflip_side'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinflip',
            name='side',
            field=models.CharField(default='head', max_length=5),
        ),
    ]
