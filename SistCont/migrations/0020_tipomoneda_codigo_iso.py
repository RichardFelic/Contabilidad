# Generated by Django 4.1.7 on 2023-04-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistCont', '0019_alter_auxiliar_transferido'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomoneda',
            name='codigo_iso',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
