# Generated by Django 5.1.2 on 2024-10-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_alter_modelvideo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelvideo',
            name='image',
            field=models.ImageField(default='polls/images/naruto', null=True, upload_to='polls/images/'),
        ),
    ]