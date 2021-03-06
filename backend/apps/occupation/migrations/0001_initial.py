# Generated by Django 3.2.9 on 2021-11-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('position_name', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('fire_date', models.DateField()),
                ('salary', models.IntegerField(verbose_name='Salary(rub)')),
                ('fraction', models.IntegerField(verbose_name='fraction(%)')),
                ('base', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('by_hours', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Occupation',
                'verbose_name_plural': 'Occupation',
                'ordering': ['name'],
            },
        ),
    ]
