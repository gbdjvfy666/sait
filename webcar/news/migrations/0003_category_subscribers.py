# Generated by Django 5.0.2 on 2024-03-12 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_alter_articles_options_author_post_comment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]