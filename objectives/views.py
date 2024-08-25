from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

objectives = [
    {
        "id": 1,
        "details": "Leer un libro de IA",
        "period": "monthly",
        "frequency": 2,
        "icon": "📚",
        "objective": "Terminar 2 libros",
        "deadline": "2024-12-31",
        "completed_times": 1
    },
    {
        "id": 2,
        "details": "Hacer ejercicio",
        "period": "daily",
        "frequency": 1,
        "icon": "💪",
        "objective": "Ejercicio diario durante 30 días",
        "deadline": "2024-09-30",
        "completed_times": 10
    },
    {
        "id": 3,
        "details": "Aprender un nuevo lenguaje de programación",
        "period": "yearly",
        "frequency": 1,
        "icon": "💻",
        "objective": "Dominar TypeScript",
        "deadline": "2024-12-31",
        "completed_times": 0
    },
    {
        "id": 4,
        "details": "Meditar",
        "period": "weekly",
        "frequency": 4,
        "icon": "🧘",
        "objective": "Meditar 4 veces por semana",
        "deadline": "2024-12-31",
        "completed_times": 12
    },
    {
        "id": 5,
        "details": "Publicar en el blog",
        "period": "monthly",
        "frequency": 1,
        "icon": "📝",
        "objective": "Publicar 12 artículos",
        "deadline": "2024-12-31",
        "completed_times": 5
    },
    {
        "id": 6,
        "details": "Practicar un instrumento musical",
        "period": "daily",
        "frequency": 1,
        "icon": "🎸",
        "objective": "Practicar guitarra todos los días",
        "deadline": "2024-12-31",
        "completed_times": 20
    }
]


#OBJECTIVES API: HOME PAGE
def home(request):
    return HttpResponse('Welcome to METAS APP API')
#OBJECTIVES API: GET AND POST OBJECTIVES 
def objectives_path(request):
    if request.method == 'GET':
        return get_objectives(request)
    elif request.method == 'POST':
        return create_objective(request)
    
def get_objectives(request):
    return JsonResponse(objectives, safe=False)

def create_objective(request):
    objective = request.POST.get('objective')
    metas = ['Objective 1', 'Objective 2', 'Objective 3']
    if objective not in metas:
        metas.append(objective)
        return HttpResponse(f'Objective {objective} created successfully')
    else:
        return HttpResponse(f'Objective {objective} already exists')

#OBJECTIVES API: GET, POST, PUT, DELETE AN OBJECTIVE BY PK(ID)

def objective_path(request, pk):
    if request.method == 'GET':
        return get_objective(request, pk)
    elif request.method == 'PUT':
        return put_objective(request, pk)
    elif request.method == 'DELETE':
        delete_objective(request, pk)

def get_objective(request, pk):
    return 

def put_objective(request, pk):
    return

def delete_objective(request, pk):
    return