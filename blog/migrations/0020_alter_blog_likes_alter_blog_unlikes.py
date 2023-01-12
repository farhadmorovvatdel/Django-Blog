# Generated by Django 4.1.3 on 2023-01-12 16:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_alter_blog_likes_alter_blog_unlikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='userlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='unlikes',
            field=models.ManyToManyField(null=True, related_name='userunlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
