# Generated by Django 5.1.4 on 2024-12-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_rename_assigned_to_company_project_assigned_to_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_project',
            old_name='assigned_to_name',
            new_name='assigned_to',
        ),
    ]