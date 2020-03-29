# Generated by Django 3.0.3 on 2020-03-28 11:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('user_type', models.IntegerField(default=1)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mitsumori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mitsumori_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('m_file', models.FileField(blank=True, upload_to='create/%Y/%m/%d/')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('service_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ServiceGroup')),
            ],
        ),
        migrations.CreateModel(
            name='MitsumoriService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mitsumori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Mitsumori')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Service')),
                ('service_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ServiceGroup')),
            ],
        ),
    ]