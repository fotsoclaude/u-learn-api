# Generated by Django 4.1.2 on 2022-12-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_training_price'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='training',
            field=models.ManyToManyField(blank=True, related_name='training', to='training.training'),
        ),
    ]
