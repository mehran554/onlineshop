# Generated by Django 4.0.2 on 2023-04-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_zarinpal_authority_order_zibal_trackid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zibal_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zibal_refNumber',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
