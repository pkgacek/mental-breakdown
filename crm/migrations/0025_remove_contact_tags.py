# Generated by Django 3.0.3 on 2020-02-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_contact_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='tags',
        ),
    ]