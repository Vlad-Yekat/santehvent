# Generated by Django 2.0.3 on 2018-06-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='goodPrice',
        ),
        migrations.AddField(
            model_name='good',
            name='goodCountry',
            field=models.CharField(default='China', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodGaranty',
            field=models.CharField(default='1 year', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodGroup',
            field=models.CharField(default='Invertor', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodHladagent',
            field=models.CharField(default='R 410A', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodKG',
            field=models.CharField(default='10 kg', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodSizeIn',
            field=models.CharField(default='80*20*30', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodSizeOut',
            field=models.CharField(default='100*50*40', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodSquare',
            field=models.CharField(default='30 sq m', max_length=100),
        ),
        migrations.AddField(
            model_name='good',
            name='goodWatt',
            field=models.CharField(default='200W', max_length=100),
        ),
        migrations.AddField(
            model_name='inshop',
            name='goodPrice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='good',
            name='qoodName',
            field=models.CharField(default='FAC1212', max_length=100),
        ),
    ]
