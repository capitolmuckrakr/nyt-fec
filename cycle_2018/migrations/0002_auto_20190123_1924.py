# Generated by Django 2.1.5 on 2019-01-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_2018', '0001_squashed_0038_auto_20190115_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filing',
            name='filing_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]