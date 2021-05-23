# Generated by Django 3.2 on 2021-05-19 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_remove_categories_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercategorysubscribe',
            name='id',
        ),
        migrations.AlterField(
            model_name='usercategorysubscribe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]