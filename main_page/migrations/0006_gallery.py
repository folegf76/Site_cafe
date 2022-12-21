# Generated by Django 4.1.4 on 2022-12-21 13:29

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(default=True)),
                ('desc', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(upload_to=main_page.models.Gallery.get_file_name)),
            ],
        ),
    ]