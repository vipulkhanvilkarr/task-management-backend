# Generated by Django 5.1.4 on 2024-12-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_company_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_project',
            name='status',
            field=models.CharField(choices=[('not started', 'not started'), ('in progress', 'in progress'), ('completed', 'completed'), ('on hold', 'on hold')], default='not started', max_length=50),
        ),
    ]
