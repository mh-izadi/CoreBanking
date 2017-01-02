# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-02 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_adminbranch'),
        ('TransactionManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Customer'),
        ),
        migrations.AddField(
            model_name='branch',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManagement.AdminBranch'),
        ),
    ]
