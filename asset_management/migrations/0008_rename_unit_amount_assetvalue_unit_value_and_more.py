# Generated by Django 4.1.3 on 2023-01-12 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "market_data",
            "0003_businesssector_index_alter_marketasset_marketplace_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("asset_management", "0007_account_reference"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assetvalue",
            old_name="unit_amount",
            new_name="unit_value",
        ),
        migrations.AddField(
            model_name="asset",
            name="market_asset",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assets",
                to="market_data.marketasset",
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="account",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assets",
                to="asset_management.account",
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="tags",
            field=models.ManyToManyField(
                related_name="assets", to="asset_management.assettag"
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assets",
                to="asset_management.assettype",
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
