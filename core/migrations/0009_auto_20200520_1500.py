# Generated by Django 3.0.6 on 2020-05-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200517_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['uid']},
        ),
        migrations.AlterField(
            model_name='log',
            name='entry_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
