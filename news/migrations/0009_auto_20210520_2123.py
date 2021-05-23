# Generated by Django 3.2 on 2021-05-20 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_auto_20210519_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='subscribers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserCategorySubscribe',
        ),
    ]
