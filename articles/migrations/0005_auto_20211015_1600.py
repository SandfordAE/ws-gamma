# Generated by Django 3.2.7 on 2021-10-15 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='timetamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]