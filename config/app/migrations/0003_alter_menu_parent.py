# Generated by Django 4.2 on 2023-04-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.CharField(blank=True, max_length=100, verbose_name='parent'),
        ),
    ]