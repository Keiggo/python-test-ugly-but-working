# Generated by Django 4.0.1 on 2022-01-28 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrainsUserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(choices=[('broker', 'Broker'), ('supplier', 'Supplier'), ('customer', 'Customer')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grains User Profile',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('supply_amount', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='grains.grainsuserprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('purchase_order', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('amount_requested', models.PositiveIntegerField()),
                ('fullfilled_date', models.DateTimeField(auto_now=True)),
                ('amount_supplied', models.PositiveIntegerField(blank=True, null=True)),
                ('delivery_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=52, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('fullfilled', 'Fullfilled')], default='pending', max_length=20)),
                ('broker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fullfilled_orders', to='grains.grainsuserprofile')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='grains.grainsuserprofile')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='grains.supplier')),
            ],
        ),
    ]