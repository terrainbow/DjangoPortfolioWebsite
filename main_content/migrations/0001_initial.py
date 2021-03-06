# Generated by Django 2.1.5 on 2019-01-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('last_updated', models.DateField(verbose_name='last updated')),
                ('link', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
