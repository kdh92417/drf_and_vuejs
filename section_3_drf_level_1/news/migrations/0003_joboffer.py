# Generated by Django 3.2.4 on 2021-07-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210714_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('job_description', models.TextField()),
                ('salary', models.IntegerField(blank=True)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
