# Generated by Django 5.1.4 on 2024-12-19 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Jumbi', max_length=15),
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=10)),
                ('quality', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField(auto_now=True)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giver', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('plot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SRSapp.plot')),
            ],
        ),
    ]