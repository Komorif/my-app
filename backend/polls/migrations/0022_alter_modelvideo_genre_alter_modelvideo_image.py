# Generated by Django 5.1.2 on 2024-10-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_alter_modelvideo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelvideo',
            name='genre',
            field=models.CharField(choices=[('educational', 'educational'), ('entertaining', 'entertaining'), ('informational', 'informational')], default='informational', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='modelvideo',
            name='image',
            field=models.ImageField(default='naruto', null=True, upload_to='polls/images/'),
        ),
    ]
