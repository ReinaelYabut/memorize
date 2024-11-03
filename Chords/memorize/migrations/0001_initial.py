# Generated by Django 4.2.10 on 2024-11-03 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChordImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='chord_images/')),
                ('chord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='memorize.chord')),
            ],
        ),
        migrations.AddField(
            model_name='chord',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chords', to='memorize.key'),
        ),
    ]