# Generated by Django 2.1.1 on 2018-09-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mfg',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
