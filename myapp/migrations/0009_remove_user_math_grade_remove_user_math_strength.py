# Generated by Django 4.2.4 on 2023-09-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_user_has_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='math_grade',
        ),
        migrations.RemoveField(
            model_name='user',
            name='math_strength',
        ),
    ]
