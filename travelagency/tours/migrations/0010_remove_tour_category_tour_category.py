# Generated by Django 4.2.1 on 2023-06-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_category_remove_tour_is_hot_tour_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='category',
        ),
        migrations.AddField(
            model_name='tour',
            name='category',
            field=models.ManyToManyField(null=True, to='tours.category'),
        ),
    ]
