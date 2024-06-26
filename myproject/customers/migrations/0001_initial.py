# Generated by Django 5.0.4 on 2024-05-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('opt_in_emails', models.BooleanField(default=False)),
                ('opt_in_sms', models.BooleanField(default=False)),
            ],
        ),
    ]
