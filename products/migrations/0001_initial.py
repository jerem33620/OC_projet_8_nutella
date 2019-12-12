# Generated by Django 3.0 on 2019-12-11 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('nutrition_grade_fr', models.CharField(max_length=3)),
                ('url', models.URLField(max_length=255)),
                ('image_url', models.URLField(max_length=255)),
                ('image_nutrition_url', models.URLField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
        ),
    ]
