# Generated by Django 5.1.4 on 2024-12-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Mobile_no', models.CharField(max_length=12)),
                ('Resume', models.FileField(upload_to='resume/')),
            ],
        ),
    ]