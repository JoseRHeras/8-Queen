# Generated by Django 3.1.2 on 2020-10-22 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201022_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='github_link_url',
            new_name='github_url',
        ),
        migrations.RenameField(
            model_name='contact_info',
            old_name='linked_in_url',
            new_name='linkedIn_url',
        ),
    ]