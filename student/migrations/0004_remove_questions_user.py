# Generated by Django 4.2.5 on 2023-09-25 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_questions_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='user',
        ),
    ]