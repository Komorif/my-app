# Generated by Django 5.1.2 on 2024-10-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_choice_question_delete_product_delete_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelvideo',
            name='month',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
