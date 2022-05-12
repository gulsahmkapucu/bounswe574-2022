# Generated by Django 4.0.4 on 2022-05-12 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='downvoters',
            field=models.ManyToManyField(related_name='article_downvoter_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='upvoters',
            field=models.ManyToManyField(related_name='article_upvoter_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
