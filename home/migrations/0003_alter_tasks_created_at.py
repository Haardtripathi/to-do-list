# Generated by Django 5.0.2 on 2024-02-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tasks_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
