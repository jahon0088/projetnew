# Generated by Django 4.2 on 2023-04-29 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_user_options_remove_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]
