# Generated by Django 2.0.2 on 2018-03-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180322_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=45)),
                ('pwd', models.CharField(max_length=45)),
                ('email', models.EmailField(default='yourmail@gmail.com', max_length=140)),
                ('name', models.CharField(default='Name', max_length=45)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]