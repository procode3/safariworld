# Generated by Django 4.2.1 on 2023-06-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_amenity_image_alter_itinerary_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='is_confimed',
            new_name='is_confirmed',
        ),
    ]
