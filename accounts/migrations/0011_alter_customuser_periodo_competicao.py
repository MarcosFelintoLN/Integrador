# Generated by Django 4.1.5 on 2023-01-17 16:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser_periodo_alter_customuser_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='periodo',
            field=models.CharField(choices=[('1', '1º Período'), ('2', '2º Período'), ('3', '3º Período'), ('4', '4º Período')], max_length=1),
        ),
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome da competição')),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]