# Generated by Django 5.1.8 on 2025-04-06 14:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_list_db',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='group_list_db',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708)),
        ),
        migrations.AddField(
            model_name='project_list_db',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project_list_db',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708)),
        ),
        migrations.AlterField(
            model_name='group_list_db',
            name='created_by',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='group_list_db',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708)),
        ),
        migrations.AlterField(
            model_name='project_list_db',
            name='created_by',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project_list_db',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708)),
        ),
        migrations.CreateModel(
            name='meeting_notes_db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meeting_date', models.DateField(blank=True)),
                ('log', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708))),
                ('created_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(blank=True, default=datetime.datetime(2025, 4, 6, 21, 35, 30, 130708))),
                ('updated_by', models.CharField(max_length=100)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kanban.group_list_db')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kanban.project_list_db')),
            ],
        ),
    ]
