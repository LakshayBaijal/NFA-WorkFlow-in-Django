# Generated by Django 4.2 on 2023-05-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFAApp', '0004_alter_entry_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='project_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
