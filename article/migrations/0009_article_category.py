# Generated by Django 3.1.2 on 2020-11-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('1', 'Cybersecurity'), ('2', 'Software')], default='1', max_length=40),
        ),
    ]
