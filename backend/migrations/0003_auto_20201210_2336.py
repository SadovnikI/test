# Generated by Django 3.1.3 on 2020-12-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20201210_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercabinet',
            name='avatar',
            field=models.ImageField(default='avatars/1.jpg', upload_to='', verbose_name='Avatar'),
        ),
    ]
