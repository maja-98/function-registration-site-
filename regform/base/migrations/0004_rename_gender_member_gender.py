# Generated by Django 4.0.3 on 2022-05-21 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_sex_member_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='Gender',
            new_name='gender',
        ),
    ]
