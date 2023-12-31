# Generated by Django 4.2.2 on 2023-07-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("preprocesos", "0009_rawprojectquasiaerea_rawprojectquasiterreno_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rawprojectquasiterreno",
            name="tipo_intersection",
            field=models.CharField(
                choices=[
                    ("original", "Original"),
                    ("nomenclatura", "Por nomenclatura"),
                    ("coordenadas", "Por coordenadas"),
                ],
                default="original",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="typerawprojectquasi",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("nivelacion", "Nivelación"),
                    ("gravterrabs", "Gravedad terrestre absoluta"),
                    ("gravterrrel", "Gravedad terrestre relativa"),
                    ("gravedades", "Gravedades terrestres absolutas y relativas"),
                ],
                max_length=15,
                unique=True,
            ),
        ),
    ]
