# Generated by Django 4.1.3 on 2022-12-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disneyapp', '0003_masahiroalgorithm_yudaialgorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masahiroalgorithm',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='wadaalgorithm',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='yudaialgorithm',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
