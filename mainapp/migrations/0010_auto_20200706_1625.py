# Generated by Django 3.0.5 on 2020-07-06 13:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20200702_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='text',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hello',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='url'),
        ),
    ]
