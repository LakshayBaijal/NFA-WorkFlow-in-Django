# Generated by Django 4.2 on 2023-05-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFAApp', '0011_vendors_delete_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='FillName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]