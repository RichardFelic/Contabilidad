# Generated by Django 4.1.7 on 2023-04-10 03:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('SistCont', '0001_initial'), ('SistCont', '0002_auto_20230306_2342'), ('SistCont', '0003_remove_tipocuenta_tipo_moneda'), ('SistCont', '0004_catalogoauxiliares'), ('SistCont', '0005_alter_auxiliar_id_alter_catalogoauxiliares_id_and_more'), ('SistCont', '0006_alter_catalogoauxiliares_descripcion'), ('SistCont', '0007_alter_catalogoauxiliares_descripcion'), ('SistCont', '0008_remove_catalogoauxiliares_identificador_and_more'), ('SistCont', '0009_auxiliar_fecha'), ('SistCont', '0010_rename_nombre_auxiliar_nombre_aux'), ('SistCont', '0011_alter_catalogoauxiliares_id_ec'), ('SistCont', '0012_alter_auxiliar_cuenta')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMoneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('ultima_tasa_cambiaria', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('origen', models.CharField(choices=[('DB', 'DB'), ('CR', 'CR')], max_length=2)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoCuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('tipo_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistCont.tipocuenta')),
                ('permite_transacciones', models.BooleanField(default=True)),
                ('nivel', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('cuenta_mayor', models.CharField(max_length=50)),
                ('balance', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoAuxiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('cuenta', models.CharField(max_length=50, null=True)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('id_EC', models.CharField(max_length=10, unique=True)),
                ('id_aux', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], null=True)),
                ('monto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('origen', models.CharField(choices=[('DB', 'DB'), ('CR', 'CR')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_aux', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistCont.tipocuenta', null=True)),
                ('id_aux', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1)),
                ('monto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('origen', models.CharField(choices=[('DB', 'DB'), ('CR', 'CR')], max_length=2, null=True)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]