# Generated by Django 2.2.1 on 2019-07-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funccrud', '0002_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('일반', '일반'), ('공지', '공지'), ('과제', '과제')], default='일반', max_length=20),
        ),
    ]
