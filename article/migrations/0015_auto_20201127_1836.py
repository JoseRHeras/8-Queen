# Generated by Django 3.1.2 on 2020-11-28 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20201127_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullarticle',
            old_name='short_article',
            new_name='article_brief',
        ),
    ]
