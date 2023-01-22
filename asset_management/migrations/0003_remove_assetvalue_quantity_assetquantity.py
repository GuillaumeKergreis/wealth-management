# Generated by Django 4.1.3 on 2022-12-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("asset_management", "0002_alter_account_account_number_alter_account_bic_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assetvalue",
            name="quantity",
        ),
        migrations.CreateModel(
            name="AssetQuantity",
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
                ("date", models.DateField()),
                ("quantity", models.FloatField()),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="asset_quantities",
                        to="asset_management.asset",
                    ),
                ),
            ],
        ),
    ]