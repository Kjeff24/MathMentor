# Generated by Django 4.2.4 on 2023-08-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_pastquestion_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastquestion',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]