# Generated by Django 3.0.7 on 2020-06-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisresults',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
