# Generated by Django 4.1.7 on 2023-03-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionmodel',
            name='prediction_house_price',
            field=models.FloatField(default=0.0),
        ),
    ]