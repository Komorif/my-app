# Generated by Django 5.1.2 on 2024-10-21 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_modelvideo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelvideo',
            name='genre',
            field=models.CharField(choices=[('развлекательный', 'entertaining'), ('образовательный', 'educational'), ('информационный', 'informational')], default='информационный', max_length=50, null=True),
        ),
    ]
