# Generated by Django 2.0.9 on 2018-11-13 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0006_mailbox_last_polling'),
        ('crm', '0019_auto_20181110_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_mailbox.Message')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Employee')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Project')),
            ],
            bases=('django_mailbox.message',),
        ),
    ]