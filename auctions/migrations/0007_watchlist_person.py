# Generated by Django 3.2.12 on 2024-02-09 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='person',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='auctions.user'),
            preserve_default=False,
        ),
    ]
