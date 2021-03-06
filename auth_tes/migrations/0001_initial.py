# Generated by Django 3.2.5 on 2021-07-13 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('imageName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodCategory', models.CharField(max_length=30)),
                ('svgName', models.CharField(max_length=30)),
                ('food_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_tes.fooditem')),
            ],
        ),
    ]
