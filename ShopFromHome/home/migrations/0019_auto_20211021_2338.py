# Generated by Django 3.2.8 on 2021-10-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211020_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='receive',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ItemUnavailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.requests')),
            ],
        ),
    ]
