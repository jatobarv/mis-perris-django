# Generated by Django 2.1.2 on 2018-10-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181024_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.TextField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='Rescatado'),
        ),
    ]
