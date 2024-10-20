# Generated by Django 5.0.6 on 2024-07-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='destinations',
            field=models.ManyToManyField(blank=True, related_name='tours', to='tours.destination'),
        ),
    ]
