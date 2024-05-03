# Generated by Django 5.0.4 on 2024-05-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_produit_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='oldprix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='produit',
            name='sold',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
