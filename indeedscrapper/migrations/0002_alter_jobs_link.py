# Generated by Django 3.2.3 on 2021-06-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indeedscrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='link',
            field=models.CharField(blank=True, max_length=11250, null=True),
        ),
    ]
