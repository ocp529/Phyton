# Generated by Django 4.1 on 2022-09-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metricas', '0002_rename_secondsurname_metrics_surnames_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='stresslevel',
            field=models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High'), ('extreme', 'Extreme')], default='low', help_text='Nivel de estrés', max_length=20),
        ),
    ]
