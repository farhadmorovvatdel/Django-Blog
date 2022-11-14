# Generated by Django 4.1.3 on 2022-11-12 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_remove_unlikepost_post_remove_unlikepost_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(related_name='userlike', to=settings.AUTH_USER_MODEL),
        ),
    ]