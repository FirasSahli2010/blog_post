# Generated by Django 3.0.7 on 2020-06-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogman', '0002_auto_20200622_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtext',
            name='blog_text',
            field=models.TextField(),
        ),
    ]
