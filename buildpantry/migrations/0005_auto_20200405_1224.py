# Generated by Django 3.0.4 on 2020-04-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildpantry', '0004_auto_20200404_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='timetocook',
            field=models.DurationField(),
        ),
    ]