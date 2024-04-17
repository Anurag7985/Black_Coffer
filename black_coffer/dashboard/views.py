from django.http import JsonResponse
from .models import JsonData
from django.shortcuts import render
import requests

def dashboard(request):
    data = requests.get('http://127.0.0.1:8000/api/data/').json
    return render(request, 'index.html', {'data': data})

def get_data(request):
    # Replace 'JsonData' with your actual model name and adjust the fields accordingly
    data = JsonData.objects.values('intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city')
    return JsonResponse(list(data), safe=False)


