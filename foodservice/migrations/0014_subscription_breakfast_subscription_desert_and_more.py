# Generated by Django 4.1.2 on 2022-10-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodservice', '0013_subscriptiontype_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='breakfast',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='desert',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='dinner',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='supper',
            field=models.BooleanField(default=True),
        ),
    ]