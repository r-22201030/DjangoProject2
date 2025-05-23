# Generated by Django 5.2 on 2025-05-03 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_merge_20250502_2100'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltyProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('reward_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loyalty_program', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
