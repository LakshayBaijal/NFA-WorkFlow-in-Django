# Generated by Django 4.2 on 2023-05-10 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFAApp', '0005_vendor_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='project_name',
        ),
    ]
