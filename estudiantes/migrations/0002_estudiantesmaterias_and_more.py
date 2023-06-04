# Generated by Django 4.2.1 on 2023-06-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0001_initial'),
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudiantesMaterias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiantes')),
                ('materias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carreras.materias')),
            ],
        ),
        migrations.AddConstraint(
            model_name='estudiantesmaterias',
            constraint=models.UniqueConstraint(fields=('estudiantes', 'materias'), name='unique_estudiantes_materias'),
        ),
    ]
