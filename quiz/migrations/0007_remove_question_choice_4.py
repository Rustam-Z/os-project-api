# Generated by Django 3.2.9 on 2021-11-26 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_quiz_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_4',
        ),
    ]