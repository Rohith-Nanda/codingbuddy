# Generated by Django 4.2.4 on 2023-08-11 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]