# Generated by Django 4.0.4 on 2022-06-09 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_imagereview_reviewimage_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='reviewtag',
            table='review_tags',
        ),
    ]
