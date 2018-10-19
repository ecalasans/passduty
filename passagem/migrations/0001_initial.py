# Generated by Django 2.1.2 on 2018-10-19 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField()),
                ('idade', models.SmallIntegerField()),
                ('igc', models.CharField(max_length=20)),
                ('pesoAtual', models.IntegerField()),
                ('diagn', models.CharField(max_length=200)),
                ('dieta', models.CharField(max_length=100)),
                ('acesso', models.CharField(default='N', max_length=2)),
                ('atbMed', models.CharField(max_length=100)),
                ('ventilacao', models.CharField(default='A', max_length=2)),
                ('fototerapia', models.BooleanField(default=False)),
                ('exames', models.CharField(max_length=500)),
                ('conduta', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('-dataHora',),
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HospMed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagem.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Leito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.SmallIntegerField()),
                ('status', models.CharField(default='V', max_length=2)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagem.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('crm', models.CharField(max_length=8)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('pesoNasc', models.IntegerField()),
                ('dataNasc', models.DateField()),
                ('leito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='passagem.Leito')),
            ],
        ),
        migrations.AddField(
            model_name='hospmed',
            name='medId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagem.Medico'),
        ),
        migrations.AddField(
            model_name='anotacao',
            name='medId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagem.Medico'),
        ),
        migrations.AddField(
            model_name='anotacao',
            name='pacId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='passagem.Paciente'),
        ),
    ]