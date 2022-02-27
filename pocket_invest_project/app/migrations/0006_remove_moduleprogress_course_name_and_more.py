# Generated by Django 4.0.2 on 2022-02-27 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_moduleprogress_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduleprogress',
            name='course_name',
        ),
        migrations.AddField(
            model_name='moduleprogress',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
            preserve_default=False,
        ),
    ]
