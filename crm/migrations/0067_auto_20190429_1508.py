# Generated by Django 2.1.8 on 2019-04-29 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('crm', '0066_auto_20190429_1505'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recruiter',
            new_name='Company',
        ),
    ]