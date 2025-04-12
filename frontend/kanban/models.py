from django.db import models
from datetime import datetime

# Create your models here.

class group_list_db(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True,default=datetime.now())
    created_by = models.CharField(max_length=100,blank=True)
    updated_on = models.DateTimeField(blank=True,default=datetime.now())
    updated_by = models.CharField(max_length=100,blank=True)


class project_list_db(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(group_list_db,to_field='id',on_delete=models.DO_NOTHING)
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True,default=datetime.now())
    created_by = models.CharField(max_length=100,blank=True)
    updated_on = models.DateTimeField(blank=True,default=datetime.now())
    updated_by = models.CharField(max_length=100,blank=True)


class meeting_notes_db(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(group_list_db,to_field='id',on_delete=models.DO_NOTHING)
    project_id = models.ForeignKey(project_list_db,to_field='id',on_delete=models.DO_NOTHING)
    meeting_title = models.TextField(blank=True)
    meeting_date = models.DateField(blank=True)
    log = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True,default=datetime.now())
    created_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(blank=True,default=datetime.now())
    updated_by = models.CharField(max_length=100)


class task_list_db(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(group_list_db,to_field='id',on_delete=models.DO_NOTHING)
    project_id = models.ForeignKey(project_list_db,to_field='id',on_delete=models.DO_NOTHING)
    meeting_notes_id = models.ForeignKey(meeting_notes_db,to_field='id',blank=True,on_delete=models.DO_NOTHING)
    log = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    task_title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    task_status = models.TextField(blank=True)
    originator = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True,default=datetime.now())
    created_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(blank=True,default=datetime.now())
    updated_by = models.CharField(max_length=100)
