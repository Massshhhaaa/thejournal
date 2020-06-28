# Generated by Django 3.0.7 on 2020-06-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('img', models.ImageField(upload_to='')),
                ('excerption', models.CharField(max_length=255, verbose_name='Отрывок')),
                ('annotation', models.TextField(verbose_name='Аннотация')),
            ],
        ),
    ]
