# Generated by Django 4.2.4 on 2023-08-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_curriculum_course_requirements_course_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='curriculum',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]