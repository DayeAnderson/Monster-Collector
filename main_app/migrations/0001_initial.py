# Generated by Django 3.1.1 on 2020-10-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('element', models.CharField(max_length=100)),
                ('wyvern_type', models.CharField(max_length=100)),
                ('ferocity', models.IntegerField()),
            ],
        ),
    ]
