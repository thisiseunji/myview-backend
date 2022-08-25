# Generated by Django 4.0.4 on 2022-06-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_reviewtag_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='with_user',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='place',
            name='link',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='place',
            name='mapx',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='mapy',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='watched_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='watched_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]