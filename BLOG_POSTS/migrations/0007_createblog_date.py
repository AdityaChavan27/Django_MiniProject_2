# Generated by Django 2.1.5 on 2020-06-06 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0006_remove_createblog_date_of_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
