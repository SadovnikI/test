# Generated by Django 3.1.3 on 2020-12-13 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=None, verbose_name='Text')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('movie_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.movie', verbose_name='Movie id')),
                ('user_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User id')),
                ('video_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.video', verbose_name='Video id')),
            ],
        ),
    ]
