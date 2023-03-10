# Generated by Django 4.1.5 on 2023-01-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата расчета')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Курс доллара к биткоину')),
                ('net_assets', models.DecimalField(decimal_places=3, max_digits=30, verbose_name='Стоимость чистых активов')),
                ('pnl', models.DecimalField(decimal_places=3, max_digits=30, verbose_name='Прибыль / убыток')),
                ('index_pnl', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Отношение чистых активов')),
            ],
            options={
                'verbose_name': 'Расчет',
                'verbose_name_plural': 'Расчеты',
                'ordering': ('-date',),
            },
        ),
    ]
