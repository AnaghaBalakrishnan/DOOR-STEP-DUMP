# Generated by Django 4.2.2 on 2023-07-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='cardname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='cardnumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='cvv',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='exp',
            field=models.IntegerField(null=True),
        ),
    ]
