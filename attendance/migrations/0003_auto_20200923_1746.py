# Generated by Django 3.0.8 on 2020-09-23 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_profile_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='is_ckecker',
            new_name='is_checker',
        ),
    ]
