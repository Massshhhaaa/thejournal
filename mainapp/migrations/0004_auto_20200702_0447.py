# Generated by Django 3.0.7 on 2020-07-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200701_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
