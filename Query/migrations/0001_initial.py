# Generated by Django 3.0.5 on 2020-11-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('query', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
