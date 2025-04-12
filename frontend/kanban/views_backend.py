from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def json_meeting_notes(request):
	from datetime import datetime
	meeting_notes_data = meeting_notes_db.objects.all()

	#get values untuk filter
	draw = int(request.GET.get('draw', 0))
	start = int(request.GET.get('start', 0))
	length = int(request.GET.get('length', 50))
	search_value = request.GET.get('search[value]', '')
	order_column_index = int(request.GET.get('order[0][column]', 0))
	order_direction = request.GET.get('order[0][dir]', 'desc')

	queryset = meeting_notes_data
	if search_value:
		queryset = queryset.filter(
			Q(group_id__group_name__icontains=search_value) |
			Q(group_id__description__icontains=search_value) |
			Q(project_id__project_name__icontains=search_value) |
			Q(project_id__description__icontains=search_value) |
			Q(meeting_date__icontains=search_value) |
			Q(log__icontains=search_value) |
			Q(notes__icontains=search_value)
			# Q(complete_log__icontains=search_value)
		)
	total_records = queryset.count()
	filtered_records = queryset.count()

	order_column = request.GET.get(f'-columns[{order_column_index}][data]', '-meeting_date')
	if order_direction == 'asc':
		order_column = f'-{order_column}'
	queryset = queryset.order_by(order_column)

	queryset = queryset[start:start + length]
	data = list(queryset.values())

	return JsonResponse({'data':data,
						 'draw':draw,
						 'recordsTotal':total_records,
						 'recordsFiltered':filtered_records})