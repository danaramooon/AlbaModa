# Generated by Django 2.1.1 on 2018-11-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_src',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
