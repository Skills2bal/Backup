# Generated by Django 4.0.4 on 2022-07-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depense',
            name='depense_date',
            field=models.DateField(auto_now_add=True, db_column='Depense_date', null=True),
        ),
    ]
