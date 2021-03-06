# Generated by Django 3.2.4 on 2021-07-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_author', models.CharField(max_length=60)),
                ('quote_body', models.TextField()),
                ('context', models.CharField(max_length=60)),
                ('source', models.URLField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
