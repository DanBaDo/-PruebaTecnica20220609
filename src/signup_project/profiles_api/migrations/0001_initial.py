# Generated by Django 4.0.5 on 2022-06-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='real name')),
                ('surname', models.CharField(max_length=200, verbose_name='last name')),
                ('email', models.EmailField(max_length=200, verbose_name='e-mail address')),
                ('phone', models.CharField(max_length=15, verbose_name='phone number')),
                ('validated_email', models.BooleanField(default=False, verbose_name='validated e-mail')),
                ('validated_phone', models.BooleanField(default=False, verbose_name='validated phone number')),
            ],
        ),
    ]
