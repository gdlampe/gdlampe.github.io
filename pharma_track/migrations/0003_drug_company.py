# Generated by Django 2.0.5 on 2018-09-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_track', '0002_auto_20180911_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='company',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
