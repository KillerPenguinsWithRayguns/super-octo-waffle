# Generated by Django 2.2.4 on 2020-04-29 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotableQuotesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='name',
            new_name='quoterName',
        ),
        migrations.AddField(
            model_name='quote',
            name='quote',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_uploaded', to='quotableQuotesApp.User'),
        ),
    ]
