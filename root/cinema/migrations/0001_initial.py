# Generated by Django 4.2.19 on 2025-02-21 09:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField(help_text='Total seats.')),
                ('wheelchair_access', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('duration', models.DurationField()),
                ('age_rating', models.CharField(choices=[('TP', 'Todos los Públicos'), ('M-7', 'Mayores de 7'), ('M-12', 'Mayores de 12'), ('M-13', 'Mayores de 13'), ('M-16', 'Mayores de 16'), ('M-18', 'Mayores de 18')], max_length=10)),
                ('original_language', models.CharField(max_length=50)),
                ('subtitles_language', models.CharField(blank=True, max_length=50, null=True)),
                ('format', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('4DX', '4DX'), ('IMAX', 'IMAX')], max_length=10)),
                ('release', models.DateField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('row', models.CharField(max_length=2)),
                ('number', models.PositiveIntegerField()),
                ('is_accessible', models.BooleanField(default=False)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.hall')),
            ],
            options={
                'unique_together': {('hall', 'row', 'number')},
            },
        ),
    ]
