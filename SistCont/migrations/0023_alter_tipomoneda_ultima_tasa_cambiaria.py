# Generated by Django 4.1.7 on 2023-04-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistCont', '0022_alter_tipomoneda_ultima_tasa_cambiaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomoneda',
            name='ultima_tasa_cambiaria',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
