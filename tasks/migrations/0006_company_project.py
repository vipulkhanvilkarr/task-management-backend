# Generated by Django 5.1.4 on 2024-12-06 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('not started', 'not started'), ('in progress', 'in progress'), ('completed', 'completed'), ('on hold', 'on hold')], default='not started', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('priority', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='low', max_length=50)),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_projects', to='tasks.user')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to='tasks.user')),
            ],
        ),
    ]
