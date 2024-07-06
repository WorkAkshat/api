from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.http import JsonResponse
import time
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.crypto import get_random_string
import requests

# Create your views here.

def tr_viewset(request):
    return render(request, 'tr_viewset.html', {})
