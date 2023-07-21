# Generated by Django 4.2.2 on 2023-07-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasteLockly', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'verbose_name_plural': 'Snippet'},
        ),
        migrations.AlterField(
            model_name='snippet',
            name='url',
            field=models.URLField(max_length=50, unique=True),
        ),
    ]