# Generated by Django 4.2.5 on 2023-09-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0007_predictdata_model_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictdata',
            name='model_type',
        ),
        migrations.AddField(
            model_name='importdata',
            name='model_type',
            field=models.CharField(default='test', max_length=10, verbose_name='Вид модели (лайт или полная)'),
            preserve_default=False,
        ),
    ]
