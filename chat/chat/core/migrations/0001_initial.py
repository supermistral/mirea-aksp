# Generated by Django 4.1.2 on 2022-10-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_code', models.CharField(blank=True, max_length=40, unique=True)),
            ],
        ),
    ]
