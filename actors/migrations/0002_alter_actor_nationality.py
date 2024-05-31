# Generated by Django 5.0.6 on 2024-05-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('EUA', 'Estados Unidos'), ('BR', 'Brasil'), ('GB', 'Reino Unido'), ('DE', 'Alemanha'), ('IL', 'Israel')], max_length=100, null=True),
        ),
    ]