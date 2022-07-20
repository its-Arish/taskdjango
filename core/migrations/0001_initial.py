

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("sale", models.IntegerField()),
                ("country", models.CharField(max_length=30, null=True)),
                ("product", models.CharField(max_length=200, null=True)),
            ],
            options={
                "ordering": ("year",),
            },
        ),
    ]
