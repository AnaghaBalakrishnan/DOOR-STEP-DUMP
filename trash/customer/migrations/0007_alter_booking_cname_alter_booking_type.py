# Generated by Django 4.2.2 on 2023-07-11 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0006_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.categories'),
        ),
    ]
