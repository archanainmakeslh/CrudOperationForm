# Generated by Django 3.2.16 on 2023-06-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
