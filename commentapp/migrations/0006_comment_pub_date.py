# Generated by Django 3.2.1 on 2021-09-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0005_auto_20210926_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='data published'),
        ),
    ]
