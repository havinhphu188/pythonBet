from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   text = """login index</h1>"""
   return HttpResponse(text)
