# Generated by Django 3.0.5 on 2020-11-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0002_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=100)),
            ],
        ),
    ]
