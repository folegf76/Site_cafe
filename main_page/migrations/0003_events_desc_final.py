# Generated by Django 4.1.4 on 2022-12-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_events_whyour_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='desc_final',
            field=models.TextField(default='000000', max_length=200),
            preserve_default=False,
        ),
    ]
