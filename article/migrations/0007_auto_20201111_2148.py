# Generated by Django 3.1.2 on 2020-11-12 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_remove_articleparagraph_carousel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullarticle',
            old_name='ending_paragaph',
            new_name='ending_paragraph',
        ),
    ]