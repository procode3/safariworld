# Generated by Django 4.2.1 on 2023-05-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
