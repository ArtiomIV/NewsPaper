# Generated by Django 3.2 on 2021-05-18 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_usercategorysubscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='subscribers',
        ),
    ]