# Generated by Django 5.1.4 on 2024-12-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_company_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_project',
            old_name='assigned_to',
            new_name='assigned_to_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('super admin', 'super admin'), ('admin', 'admin'), ('user', 'user')], default='user', max_length=50),
        ),
    ]
