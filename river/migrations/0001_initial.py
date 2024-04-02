# Generated by Django 5.0.3 on 2024-04-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='River',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('river_name', models.CharField(max_length=20)),
                ('river_length', models.IntegerField()),
                ('river_area', models.IntegerField()),
                ('flows_in_states', models.CharField(max_length=20)),
                ('river_mode', models.CharField(choices=[('Perennial', 'PERENNIAL'), ('Seasonal', 'SEASONAL')], max_length=10)),
            ],
        ),
    ]
