# Generated by Django 3.0.7 on 2020-07-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200702_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]