# Generated by Django 2.0 on 2019-08-09 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_snippet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='code',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
    ]