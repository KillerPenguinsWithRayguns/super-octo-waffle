# Generated by Django 2.2.4 on 2020-04-28 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmPassword',
        ),
    ]