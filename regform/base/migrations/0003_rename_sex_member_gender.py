# Generated by Django 4.0.3 on 2022-05-21 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_member_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='sex',
            new_name='Gender',
        ),
    ]
