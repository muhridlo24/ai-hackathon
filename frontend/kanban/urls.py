from django.urls import path,include
from . import views
from . import views_backend as vwb

urlpatterns = [
    path('',view=views.main_menu_page,name='main_menu_page'),
    path('kanban/',view=views.kanban_page,name='kanban_main_page'),
    path('overview/',view=views.home_page,name='home_page'),
    path('meeting-notes/',view=views.meeting_notes_page,name='meeting_notes_page'),
    path('groups/',view=views.groups_page,name='groups_page')
]