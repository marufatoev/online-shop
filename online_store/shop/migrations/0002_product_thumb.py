# Generated by Django 4.0.4 on 2022-06-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]