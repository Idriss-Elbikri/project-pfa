# Generated by Django 5.0.4 on 2024-05-02 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_produit_oldprix_alter_produit_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='oldprix',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='sold',
        ),
    ]
