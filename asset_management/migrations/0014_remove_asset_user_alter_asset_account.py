# Generated by Django 4.1.3 on 2023-01-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("asset_management", "0013_alter_accountvalue_account_transaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="asset",
            name="user",
        ),
        migrations.AlterField(
            model_name="asset",
            name="account",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assets",
                to="asset_management.account",
            ),
            preserve_default=False,
        ),
    ]
