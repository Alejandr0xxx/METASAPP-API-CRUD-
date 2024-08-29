from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Objectives
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict
#OBJECTIVES API: HOME PAGE
def home(request):
    return HttpResponse('Welcome to METAS APP API')
#OBJECTIVES API: GET AND POST OBJECTIVES 
@csrf_exempt
def objectives_path(request):
    if request.method == 'GET':
        return get_objectives(request)
    elif request.method == 'POST':
        return create_objective(request)

def get_objectives(request):
    objectives = list(Objectives.objects.all().values())
    return JsonResponse(objectives, safe=False)
def create_objective(request):
    data = json.loads(request.body)
    details = data.get('details')
    id = data.get('id')
    if len(details) < 5:
        return JsonResponse({'error':'Details must have at least 5 characters'}, status=400)
    elif id:
        return JsonResponse({'error': 'ID field is not required'}, status=400)
    Objectives.objects.create(**data)
    return JsonResponse(data, status=201)

#OBJECTIVES API: GET, POST, PUT, DELETE AN OBJECTIVE BY PK(ID)
@csrf_exempt
def objective_path(request, pk):
    if request.method == 'GET':
        return get_objective(request, pk)
    elif request.method == 'PUT':
        return put_objective(request, pk)
    elif request.method == 'DELETE':
        return delete_objective(request, pk)

def get_objective(request, pk):
    objective = get_object_or_404(Objectives, id=pk)
    return JsonResponse(model_to_dict(objective))

def put_objective(request, pk):
    data = json.loads(request.body)
    details = data.get('details')
    id = data.get('id')
    if len(details) < 5:
        return JsonResponse({'error':'Details must have at least 5 characters'}, status=400)
    elif id:
        return JsonResponse({'error': 'ID field is not required'}, status=400)    
    get_object_or_404(Objectives, id=pk)
    Objectives.objects.filter(id=pk).update(**data)
    return JsonResponse(data, status=200)

def delete_objective(request, pk):
    get_object_or_404(Objectives, id=pk).delete()
    return JsonResponse({'message': 'Objective deleted successfully'}, status=204)
