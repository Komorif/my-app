# Generated by Django 5.1.2 on 2024-10-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_modelvideo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelvideo',
            name='genre',
            field=models.CharField(choices=[('entertaining', 'entertaining'), ('informational', 'informational'), ('educational', 'educational')], default='informational', max_length=50, null=True),
        ),
    ]