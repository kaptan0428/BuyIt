# Generated by Django 3.2.8 on 2021-10-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211018_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
