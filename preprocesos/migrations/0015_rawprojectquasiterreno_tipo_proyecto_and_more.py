# Generated by Django 4.2.2 on 2023-07-19 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("preprocesos", "0014_alter_rawdataquasiterreno_nomenclatura"),
    ]

    operations = [
        migrations.AddField(
            model_name="rawprojectquasiterreno",
            name="tipo_proyecto",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proyectos_crudos_quasigeodales_terreno_tipo_proyecto",
                to="preprocesos.typerawprojectquasi",
            ),
        ),
        migrations.AlterField(
            model_name="rawprojectquasiterreno",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="proyectos_crudos_quasigeodales_terreno_usuario",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
