# Generated by Django 3.0.7 on 2020-06-22 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BirdieApp', '0003_disc_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='recipient_id',
            new_name='recipient',
        ),
    ]