# Generated by Django 4.1 on 2022-08-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='id',
        ),
        migrations.RemoveField(
            model_name='equipement',
            name='categorie_categorie',
        ),
        migrations.AddField(
            model_name='categorie',
            name='categorie_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
