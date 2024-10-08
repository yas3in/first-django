# Generated by Django 5.1 on 2024-08-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_name',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
