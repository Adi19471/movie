# Generated by Django 3.0 on 2021-06-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210609_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
