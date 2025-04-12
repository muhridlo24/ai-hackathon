from django.forms import ModelForm
from .models import *


class task_list_form(ModelForm):
    class Meta:
        model = task_list_db
        fields = '__all__'


class meeting_notes_form(ModelForm):
    class Meta:
        model = meeting_notes_db
        fields = '__all__'


class project_list_form(ModelForm):
    class Meta:
        model = project_list_db
        fields = '__all__'


class group_list_form(ModelForm):
    class Meta:
        model = group_list_db
        fields = '__all__'