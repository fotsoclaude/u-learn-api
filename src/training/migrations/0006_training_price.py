# Generated by Django 4.1.2 on 2022-12-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_alter_tag_training'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
