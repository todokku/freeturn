# Generated by Django 2.0.9 on 2018-12-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0027_cv_cvgenerationsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_title',
            field=models.CharField(default='Freelance python developer', help_text='Default title to use',
                                   max_length=255),
        ),
    ]