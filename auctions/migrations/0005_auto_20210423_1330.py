# Generated by Django 3.1.2 on 2021-04-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210423_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bids',
            field=models.ManyToManyField(blank=True, null=models.IntegerField(), related_name='bids_in_the_auction', to='auctions.Bid'),
        ),
    ]