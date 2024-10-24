# Generated by Django 5.1.2 on 2024-10-21 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_remove_modelvideo_image_alter_modelvideo_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelvideo',
            name='image',
            field=models.ImageField(default='naruto', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='modelvideo',
            name='genre',
            field=models.CharField(choices=[('entertaining', 'entertaining'), ('educational', 'educational'), ('informational', 'informational')], default='informational', max_length=50, null=True),
        ),
    ]
