# Generated by Django 3.2.7 on 2021-10-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
