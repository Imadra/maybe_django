# Generated by Django 2.0.2 on 2018-03-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='./mainpage/static/img/products_img/'),
        ),
    ]