# Generated by Django 3.0.4 on 2020-03-21 22:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='consumerlaw',
            name='content',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
        migrations.AlterField(
            model_name='consumerlaw',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='creditrepair',
            name='content',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
        migrations.AlterField(
            model_name='creditrepair',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='services',
            name='content',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=300),
        ),
    ]