# Generated by Django 4.1.2 on 2022-10-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
