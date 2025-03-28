# Generated by Django 5.1.7 on 2025-03-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codCarrera', models.CharField(max_length=255)),
                ('codAnio', models.CharField(max_length=255)),
                ('codAlumno', models.CharField(max_length=255)),
                ('priNombre', models.CharField(max_length=255)),
                ('segNombre', models.CharField(max_length=255)),
                ('priApellido', models.CharField(max_length=255)),
                ('segApellido', models.CharField(max_length=255)),
                ('telefono', models.BigIntegerField()),
                ('correo', models.CharField(max_length=255)),
                ('fechaNac', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fecha_actulizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'estudiante',
                'ordering': ['-created_at'],
            },
        ),
    ]
