# Generated by Django 5.0.3 on 2024-04-15 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0002_alumno_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='apellido',
            new_name='apellido_alumno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='legajo',
            new_name='legajo_alumno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='nombre',
            new_name='nombre_alumno',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='apellido',
            new_name='apellido_profesor',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='legajo',
            new_name='legajo_profesor',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='materia',
            new_name='materia_profesor',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='nombre',
            new_name='nombre_profesor',
        ),
    ]