# Generated by Django 3.2.1 on 2021-09-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0003_auto_20210921_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
