# Generated by Django 2.0.5 on 2018-08-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("catalog", "0003_auto_20180719_0635")]

    operations = [
        migrations.AddField(
            model_name="bill", name="goodPrice", field=models.FloatField(default=0.0)
        ),
        migrations.AddField(
            model_name="invoice", name="goodPrice", field=models.FloatField(default=0.0)
        ),
    ]
