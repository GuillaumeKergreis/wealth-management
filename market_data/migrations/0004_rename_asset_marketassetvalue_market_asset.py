# Generated by Django 4.1.3 on 2023-01-12 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "market_data",
            "0003_businesssector_index_alter_marketasset_marketplace_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="marketassetvalue",
            old_name="asset",
            new_name="market_asset",
        ),
    ]