# Generated by Django 3.0.7 on 2021-07-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_alter_quote_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]