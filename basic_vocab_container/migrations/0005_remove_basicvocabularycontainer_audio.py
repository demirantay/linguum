# Generated by Django 3.1 on 2020-11-30 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_vocab_container', '0004_basicvocabularycontainer_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicvocabularycontainer',
            name='audio',
        ),
    ]
