# Generated by Django 2.0.7 on 2018-07-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_auto_20180704_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conment',
            name='source_id',
            field=models.CharField(max_length=25, verbose_name='文章id或source名称'),
        ),
        migrations.AlterField(
            model_name='conment',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='conment',
            name='url',
            field=models.CharField(max_length=100, verbose_name='链接'),
        ),
    ]
