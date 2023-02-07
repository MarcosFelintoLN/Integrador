# Generated by Django 4.1.5 on 2023-01-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default=False, max_length=1),
        ),
    ]
