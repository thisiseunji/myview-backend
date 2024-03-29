# Generated by Django 4.0.4 on 2022-09-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'country_codes',
            },
        ),
        migrations.DeleteModel(
            name='Platform',
        ),
    ]
