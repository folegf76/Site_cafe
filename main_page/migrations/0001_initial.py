# Generated by Django 4.1.4 on 2022-12-14 09:44

from django.db import migrations, models
import django.db.models.deletion
import main_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('is_special', models.BooleanField(default=False)),
                ('desc', models.TextField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ingredients', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=main_page.models.Dish.get_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.dishcategory')),
            ],
        ),
    ]
