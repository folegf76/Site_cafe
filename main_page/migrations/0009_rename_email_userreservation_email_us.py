# Generated by Django 4.1.4 on 2022-12-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_alter_userreservation_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreservation',
            old_name='email',
            new_name='email_us',
        ),
    ]
