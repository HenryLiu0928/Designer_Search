# Generated by Django 4.2.1 on 2023-05-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_demo_link_alter_project_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured_image',
        ),
    ]
