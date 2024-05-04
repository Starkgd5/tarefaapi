# Generated by Django 5.0.4 on 2024-04-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[("Pendente", 1), ("Em Andamento", 2), ("Concluido", 3)],
                default=1,
                max_length=15,
            ),
        ),
    ]