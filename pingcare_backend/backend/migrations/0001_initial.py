# Generated by Django 2.1.5 on 2019-01-19 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('text_loc', models.CharField(max_length=255)),
                ('issue', models.CharField(max_length=5000)),
                ('ping_count', models.PositiveIntegerField()),
            ],
        ),
    ]