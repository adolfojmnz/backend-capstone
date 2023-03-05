from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse
import requests, json, os

import environ

env = environ.Env()
environ.Env.read_env()


def get_auth_header():
    url = 'http://127.0.0.1:8000/api/token/login/'
    data = {
        'username': env('USERNAME'),
        'password': env('PASSWORD')
    }
    response = requests.post(url, data=data)
    response_dict = json.loads(response.text)
    token = response_dict.get('access')
    return {'Authorization': f'JWT {token}'}


def index(request):
    return render(request, 'restaurant/index.html', {})


def about(request):
    return render(request, 'restaurant/about.html')


def menu(request):
    url = f"http://127.0.0.1:8000{reverse('api:menu')}"
    headers = get_auth_header()
    response = requests.get(url, headers=headers)
    return render(request, 'restaurant/menu.html', context={'menu_items': json.loads(response.text)})

def menu_item(request, pk):
    url = f"http://127.0.0.1:8000{reverse('api:menu-detail', kwargs={'pk': pk})}"
    headers = get_auth_header()
    response = requests.get(url, headers=headers)
    return render(request, 'restaurant/menu_item.html', context={'menu_item': json.loads(response.text)})
