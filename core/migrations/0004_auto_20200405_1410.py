# Generated by Django 2.2 on 2020-04-05 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='entry_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='core.Station'),
        ),
        migrations.AlterField(
            model_name='log',
            name='exit_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exit', to='core.Station'),
        ),
        migrations.AlterField(
            model_name='log',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
    ]
