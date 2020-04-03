# Generated by Django 3.0.4 on 2020-03-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildpantry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='mealtype',
            field=models.CharField(blank=True, choices=[('Breakfast and Brunch', 'Breakfast and Brunch'), ('Desserts', 'Desserts'), ('Dinners', 'Dinners'), ('Lunch', 'Lunch')], default='', max_length=35, null=True),
        ),
    ]