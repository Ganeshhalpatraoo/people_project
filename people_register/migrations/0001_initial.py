# Generated by Django 4.0.6 on 2022-07-11 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
                ('Students', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('Father_name', models.CharField(max_length=100)),
                ('Father_occ', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('College', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people_register.position')),
            ],
        ),
    ]
