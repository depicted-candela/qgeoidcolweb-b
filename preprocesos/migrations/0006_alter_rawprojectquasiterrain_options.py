# Generated by Django 4.2.2 on 2023-07-14 21:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("preprocesos", "0005_rawprojectquasiterrain_delete_rawproject"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rawprojectquasiterrain",
            options={
                "verbose_name": "proyecto hijo para el modelo quasi-geoidal",
                "verbose_name_plural": "proyectos hijos para el modelo quasi-geoidal",
            },
        ),
    ]