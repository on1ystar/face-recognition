# Generated by Django 3.0.8 on 2020-10-05 16:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20201005_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='checkmate/user'),
        ),
    ]
