# Generated by Django 2.0.5 on 2018-09-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_track', '0003_drug_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='phase',
            field=models.CharField(choices=[('Phase 1', 'Phase 1'), ('Phase 2', 'Phase 2'), ('Phase 3', 'Phase 3'), ('Phase 4', 'Phase 4')], default='Phase 1', max_length=400),
        ),
    ]
