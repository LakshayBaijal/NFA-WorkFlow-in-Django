# Generated by Django 4.2 on 2023-05-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFAApp', '0010_vendor_delete_vendors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=20)),
                ('vendor_name', models.CharField(blank=True, max_length=20, null=True)),
                ('item_name', models.CharField(blank=True, max_length=20, null=True)),
                ('total_base_value', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.CharField(blank=True, max_length=20, null=True)),
                ('unit_of_measurement', models.CharField(blank=True, max_length=10, null=True)),
                ('freight_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('pf_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('custom_duty', models.CharField(blank=True, max_length=10, null=True)),
                ('installation_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('amc_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('third_party_inspection_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('other_charges', models.CharField(blank=True, max_length=10, null=True)),
                ('total_value', models.CharField(blank=True, max_length=10, null=True)),
                ('gst', models.CharField(blank=True, max_length=10, null=True)),
                ('landed_cost', models.CharField(blank=True, max_length=10, null=True)),
                ('delivery', models.CharField(blank=True, max_length=10, null=True)),
                ('payment_terms', models.CharField(blank=True, max_length=10, null=True)),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
