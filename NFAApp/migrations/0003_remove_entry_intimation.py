# Generated by Django 4.2 on 2023-05-10 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFAApp', '0002_alter_entry_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='intimation',
        ),
    ]
