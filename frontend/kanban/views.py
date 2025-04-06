from django.shortcuts import render

# Create your views here.

def main_menu_page(request):
    return render(request=request,template_name='main_menu_page.html')

def kanban_page(request):
    return render(request=request,template_name='kanban_board.html')

def home_page(request):
    return render(request=request,template_name='home.html')

def meeting_notes_page(request):
    return render(request=request,template_name='meeting_notes_page.html')

def groups_page(request):
    return render(request=request,template_name='groups_page.html')