# Generated by Django 4.2.1 on 2023-06-02 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0013_remove_tour_country_tour_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tours.country'),
        ),
    ]
