# Generated by Django 4.2.4 on 2023-08-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='class_level',
            field=models.CharField(blank=True, choices=[('JHS 1', 'JHS 1'), ('JHS 2', 'JHS 2'), ('JHS 3', 'JHS 3')], default='null', max_length=10, null=True),
        ),
    ]