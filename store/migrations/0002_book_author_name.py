# Generated by Django 3.0.7 on 2022-02-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Author', max_length=255),
            preserve_default=False,
        ),
    ]
