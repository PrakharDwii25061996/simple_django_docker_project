# Generated by Django 4.1.7 on 2023-07-24 07:31

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
                ('name', models.CharField(max_length=55)),
                ('price', models.FloatField(default=0, max_length=100)),
                ('description', models.TextField(null=True)),
                ('number_of_items', models.IntegerField(default=1)),
            ],
        ),
    ]
